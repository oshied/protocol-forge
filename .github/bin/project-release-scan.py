#!/usr/bin/env python3

import json
import os
import re
import sys

from collections import OrderedDict
from urllib.parse import urlparse

import requests


def _tag_api(client, owner_repo, all_tags=None, page=1):
    """Recursively retrieve all tags.

    param client: Object
    param owner_repo: String
    param all_releases: List
    param page: Integer
    returns: List
    """
    _all_tags_data = client.get(
        f"https://api.github.com/repos/{owner_repo}/tags?per_page=100&page={page}"
    )

    if not all_tags:
        all_tags = OrderedDict()

    if _all_tags_data.status_code == 200:
        all_tags_data = _all_tags_data.json()
        for item in all_tags_data:
            try:
                all_tags[item["name"]] = item["html_url"]
            except Exception:
                pass

        if len(all_tags_data) == 100:
            page += 1
            return _tag_api(
                client=client,
                owner_repo=owner_repo,
                all_tags=all_tags,
                page=page,
            )

    return all_tags


def _release_api(client, owner_repo, all_releases=None, page=1):
    """Recursively retrieve all releases.

    param client: Object
    param owner_repo: String
    param all_releases: List
    param page: Integer
    returns: List
    """
    _all_release_data = client.get(
        f"https://api.github.com/repos/{owner_repo}/releases?per_page=100&page={page}"
    )

    if not all_releases:
        all_releases = list()

    if _all_release_data.status_code == 200:
        all_release_data = _all_release_data.json()
        for item in all_release_data:
            try:
                if item["draft"] is True:
                    continue
                elif item["prerelease"] is True:
                    continue

                all_releases.append(item["tag_name"])
            except Exception:
                pass

        if len(all_release_data) == 100:
            page += 1
            return _release_api(
                client=client,
                owner_repo=owner_repo,
                all_releases=all_releases,
                page=page,
            )

    return all_releases


def _git_release_check(client, name, repo, release):
    """Run checks with the github api.

    param client: Object
    param name: String
    param repo: String
    param release: String
    returns: Object
    """
    parsed_repo = urlparse(repo)
    owner_repo = re.sub(r"^\/|(\/releases|\/archive)$", "", parsed_repo.path)
    _latest_release_data = client.get(
        f"https://api.github.com/repos/{owner_repo}/releases/latest"
    )
    latest_release_data = _latest_release_data.json()
    try:
        html_url = latest_release_data["html_url"]
    except KeyError:
        html_url = None
    try:
        tag_name = latest_release_data["tag_name"]
    except KeyError:
        tag_name = None

    all_releases = _release_api(client=client, owner_repo=owner_repo)
    all_tags = _tag_api(client=client, owner_repo=owner_repo)
    if all_tags:
        tags = all_tags.keys()
        if not tag_name:
            tag_name = tags[0]

        if not html_url:
            html_url = all_tags[tags[0]]

        if not all_releases:
            all_releases = list(tags)

    if tag_name and release != tag_name:
        return {
            "name": name.lower(),
            "repo": repo,
            "current_release": tag_name,
            "current_release_url": html_url,
            "all_releases": all_releases,
            "existing_release": release,
        }

def main():
    """Run release scan for all projects supported by figment.

    All projects are defined by by the projects.yml file within the
    group_vars/all/ directory. Each project is indexed and updated
    whenever the current release doesn't match our known value.
    """
    session = requests.Session()
    session.headers["Authorization"] = f"token {sys.argv[1].strip()}"
    session.headers["Accept"] = "application/vnd.github+json"

    updates = list()

    for sub_dir in os.listdir():
        if not os.path.isdir(sub_dir):
            continue

        try:
            with open(os.path.join(sub_dir, "Dockerfile")) as f:
                for line in f.readlines():
                    git_repository = re.search(r"^\w+\s(?:git_repository)\D(\S+)", line)
                    if git_repository:
                        git_repository = git_repository.groups()[0]
                        git_repository = re.sub(r"(.git$)", "", git_repository)
                        with open(os.path.join(sub_dir, "VERSION")) as f:
                            version = f.read().strip()
                        update = _git_release_check(
                            client=session,
                            name=sub_dir,
                            repo=git_repository,
                            release=version
                        )
                        if update:
                            updates.append(update)
                        break
        except Exception as f:
            pass

    print(json.dumps({"include": updates}))


if __name__ == "__main__":
    main()
