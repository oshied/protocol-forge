# Protocol Container Builds

This repository contains a collection of container image build files
in the `Dockerfile` format. Within this repository each directory in
the root is considered to be a container build root. If a `Dockerfile`
is found within the sub directory, the system will return it as part
of the matrixed deliverables.

When building / iterating on container images, the `VERSION` file is
used to define the "tag" when a container image is built.

> The version file is any set of ASCII characters on a single line.

### Hierarchy

The directory structure is simple

``` shell
.
└── VendoredContainerX
    ├── Dockerfile
    ├── VERSION
    └── MANIFEST
```

## Build Process

Github actions is used to build the container images, using a dynamic
matrix which is defined by items changed within the repository.

To trigger a build, all one needs to do is send a pull request with
with the new container or modify files within the context of an
existing container. This will kick off a build to validate that the
proposed change results in a build that will converge.

Once the PR is merged, the push action will once again spawn a
matrix for all changes and perform the same build action, but this
time push the built image to our registry.

Items in the MANIFEST file are extracted from the container image and
pushed to our public S3 bucket. Items in the MANIFEST file follow the
in container PATH. The base name will be extracted.

We use the following format to push extracted build files.

``` url
S3://VendoredContainerX/VERSION/MANIFEST_file
```

### Reproducing a build

Recreating a build locally is simple as everything is done within a
container.

1. Clone this repository
2. Change directory into the protocol based subdirectory
3. Run docker build for the protocol

All container build files have constant arguments.

* **git_repository** - The `git_repository` build arg is used to define the
  git repository used for the build process. In most build situations the
  `git_repository` argument will not be needed.

* **git_version** - The `git_version` build arg is defined within the VERSION
  file with the sub-directory. If there's no version file found, the
  `git_version` is expected to be **main**.

Run the build

``` shell
cd $SUB_DIRECTORY
export VERSION="$(sed 's/[[:space:]]//g' VERSION)"  # Ensures that the version file value is stripped
export PROTOCOL_NAME="$(basename $(pwd))"
docker build --build-arg git_version=${VERSION} \
             --tag ${PROTOCOL_NAME}:${VERSION} .
```

Once the build is complete binaries can be extracted or the container can
be used leveraging the entrypoint.
