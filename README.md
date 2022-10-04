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

###### Run a local build

``` shell
# Change into the sub directory for the build
cd $SUB_DIRECTORY

# Set container build information
export CONTAINER_TAG="$(sed 's/[[:space:]]//g' VERSION)"  # Ensures that the version file value is stripped

# Set the protocol name, in this example it is assumed the name is the same as the sub-directory
export PROTOCOL_NAME="$(basename $(pwd))"

# Run the build
docker build --build-arg git_version=${CONTAINER_TAG} \
             --tag ${PROTOCOL_NAME}:${CONTAINER_TAG} .
```

Once the build is complete binaries can be extracted or the container can
be used leveraging the entrypoint.

###### Example running binary extraction using the manifest file

``` shell
# Set the PROTOCOL_NAME we'll be working with

# Change to the protocol sub-directory to read the manifest file
cd $SUB_DIRECTORY

# Set the protocol name, in this example it is assumed the name is the same as the sub-directory
export PROTOCOL_NAME="$(basename $(pwd))"

# Define the image name we'll extract binaries from
export CONTAINER_NAME=$PROTOCOL_NAME

# Define the tag, this command example reads the version as the tag information
export CONTAINER_TAG=$(sed 's/[[:space:]]//g' VERSION)

# Create a container from the built image and store the ID
export CONTAINER_ID=$(docker create ${CONTAINER_NAME}:${CONTAINER_TAG} ${CONTAINER_NAME})

# Create a storage location
mkdir -p /tmp/$PROTOCOL_NAME

# Loop through the files and extract the files to our storage location
for FILE_NAME in $(sed 's/[[:space:]]//g' MANIFEST); do
  BASE_FILE_NAME="$(basename ${FILE_NAME})"
  docker cp ${CONTAINER_ID}:${FILE_NAME} /tmp/${PROTOCOL_NAME}/${BASE_FILE_NAME}
done

# Remove the temp container now that we're done with it
docker container rm ${CONTAINER_ID}
```
