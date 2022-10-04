#!/usr/bin/env python3

import json
import os
import sys


def main():
    """Take a list of inputs and print a json matrix for builds."""
    bad_versions = {}
    updates = []
    input_paths = [[i for i in os.path.split(path) if i][0] for path in sys.argv[1:]]
    input_paths = sorted(set(input_paths))
    for path in input_paths:
        item = {"base": path}
        container_file = os.path.join(path, "Dockerfile")
        if os.path.exists(container_file):
            item["file"] = container_file
            version_file = os.path.join(path, "VERSION")
            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as f:
                    git_version = item["git_version"] = f.read().strip()
                    version_str = item["version"] = git_version.split("/")[-1]
                    if not version_str:
                        bad_versions[version_file] = "Version is undefined"
            else:
                item["version"] = "latest"
            manifest_file = os.path.join(path, "MANIFEST")
            if os.path.exists(manifest_file):
                with open(manifest_file, encoding="utf-8") as f:
                    item["manifest"] = " ".join([i.strip() for i in f.readlines() if i])

            updates.append(item)

    if bad_versions:
        for file, error in bad_versions.items():
            print(f"[ERROR] {error} in file {file}", file=sys.stderr)
        sys.exit(1)
    else:
        print(json.dumps({"include": updates}))


if __name__ == "__main__":
    main()
