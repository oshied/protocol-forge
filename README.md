# Protocol Container Builds

This repository contains a collection of container image build files
in the `Dockerfile` format. Within this repository each directory in
the root is considered to be a container build root. If a `Dockerfile`
is found within the sub directory, the system will return it as part
of the matrixed deliverables.

The output of this build process is simple.

* A distroless container will be created containing all of the binaries
  and libraries needed to run a given protocol


When building / iterating on container images, the `VERSION` file is
used to define the "tag" when a container image is built.

> The version file is any set of ASCII characters on a single line.

## Hierarchy

The directory structure is simple

``` shell
.
└── VendoredContainerX
    ├── Dockerfile
    ├── VERSION
    ├── TARGETS
    ├── MANIFEST
    ├── RUNNER
    └── README.md
```

### Build Process

Github actions is used to build the container images, using a dynamic
matrix which is defined by items changed within the repository.

To trigger a build, all one needs to do is send a pull request with
with the new container or modify files within the context of an
existing container. This will kick off a build to validate that the
proposed change results in a build that will converge.

Once the PR is merged, the push action will once again spawn a
matrix for all changes and perform the same build action, but this
time push the built image to our registry.

> Items in the `TARGETS` file are used to define build targets which are
  then pushed to the registry. This is useful to define multiple build
  environments supporting different distros, or runtime specific
  requirements.

> Items in the `MANIFEST` file are extracted from the container image and
  pushed to our public S3 bucket. Items in the MANIFEST file follow the
  in container PATH. The base name will be extracted.

> Items in the `RUNNER` file (optional) are used to define the build runners
  when executing jobs in github-actions. If there's a specific protocol that
  needs a custom runner, or just something different from the default
  **ubuntu-latest**, this file is used to determine the job placement. It is
  also possible to use this file to instruct a protocol to build on multiple
  runners, runners are defined one per-line.

We use the following format to push extracted build files.

``` url
//VendoredContainerX/TARGET(S)/VERSION/MANIFEST_file
```

#### Reproducing a build

Recreating a build locally is simple as everything is done within a
container.

1. Clone this repository
2. Change directory into the protocol based subdirectory
3. Run buildah build for the protocol

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
# NOTE(cloudnull): The public GHCR repo also maintains build cache for every repository and tags it for
#                  reproduceability.
docker build --build-arg git_version=${CONTAINER_TAG} \
             --tag ${PROTOCOL_NAME}:${CONTAINER_TAG} \
             --cache-from type=registry,ref=ghcr.io/oshied/${PROTOCOL_NAME}:buildcache-target \
             .
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


###### Example Build New Debian Package

``` shell
# Change into the sub directory for the build
cd $SUB_DIRECTORY

# Set container build information
export CONTAINER_TAG="$(sed 's/[[:space:]]//g' VERSION)"  # Ensures that the version file value is stripped

# Set the protocol name, in this example it is assumed the name is the same as the sub-directory
export PROTOCOL_NAME="$(basename $(pwd))"

# Set the build maintainer. If you build a package, claim credit for it.
export BUILD_MAINTAINER="Kevin Carter <kevin@cloudnull.com>"

# Set the ExecStart path. CI will set this option to the first item in the MANIFEST but you can
# define it to be anything you want.
export BUILD_EXEC="$(head -n 1 MANIFEST)"

# create a location to retrieve the new debian package
mkdir /tmp/packages

# create a location to store the binary manifest files
mkdir /tmp/binaries

# Pull the contents of the manifest from the current container version
CONTAINER="$(docker create ghcr.io/oshied/${PROTOCOL_NAME}:${CONTAINER_TAG} ${PROTOCOL_NAME})"
for FILE_NAME in $(sed 's/[[:space:]]//g' MANIFEST | tr '\n' ' '); do
  BASE_FILE_NAME="$(basename ${FILE_NAME})"
  mkdir -p "/tmp/binaries/$(dirname ${FILE_NAME})"
  docker cp ${CONTAINER}:${FILE_NAME} /tmp/binaries/${FILE_NAME}
done

# Build the debian package
docker run -t --volume /tmp/packages:/packages:rw \
              --volume $(pwd)/../.github/bin:/srv \
              --volume /tmp/binaries:/mnt:rw \
              --env CONTAINER_TAG="${CONTAINER_TAG}" \
              --env PROTOCOL_NAME="${PROTOCOL_NAME}" \
              --env BUILD_EXEC="${BUILD_EXEC}" \
              --env BUILD_MAINTAINER="${BUILD_MAINTAINER}" \
              ghcr.io/oshied/base-dpkg:jammy \
              /srv/build-deb.sh
```

The packages created by this repo will install the protocol binaries,
any required libraries, create a protocol specific user, touches a
defaults file, and generates a systemd service unit.

To use the systemd service unit, it is expected that the deployer
uses the defaults file for any and all environment variables needed
to be passed through to the protocol when running as a daemon. The
defaults file can be found at `/etc/defaults/PROTOCOL_NAME`.

Additionally, the default `ExecStart` isn't intended to be fully complete
out of the box. To customize the `ExecStart`, or any other systemd parameter,
create an override file in `/etc/systemd/system/PROTOCOL_NAME.service.d/`.

For example to change the `ExecStart` call

``` conf
cat > /etc/systemd/system/PROTOCOL_NAME.service.d/override.conf <<EOF
[Service]
ExecStart=
ExecStart=/usr/local/bin/PROTOCOL_NAME run
EOF
```

> While the default `ExecStart` is not intended to be used, the executable for
  the used is the first item in within the **MANIFEST** file of a given
  protocol.

This drop-in will wipeout the original `ExecStart` call and replace it.
From the systemd point of view, the override configuration file is seen
as part of the service

``` shell
systemctl status PROTOCOL_NAME
● PROTOCOL_NAME.service - Container PROTOCOL_NAME
     Loaded: loaded (/etc/systemd/system/PROTOCOL_NAME.service; disabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/PROTOCOL_NAME.service.d
             └─override.conf
```

Drop-in override configuration files can be used to change or modify
anything within the systemd service unit file.

Every protocol will have a user created with a home directory at
`/var/lib/PROTOCOL_NAME`. This is the expected location where all of
the service specific configuration and data will live.
