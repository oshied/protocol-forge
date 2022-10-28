FROM ghcr.io/oshied/base-build:bionic as bionic
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
ARG name="base-rocksdb"
ARG summary="Base build image for rocksdb built on-top of ubuntu Bionic"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      app.kubernetes.io/version="${git_version}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN PORTABLE=1 DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared

FROM ghcr.io/oshied/base-build:focal as focal
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
ARG name="base-rocksdb"
ARG summary="Base build image for rocksdb built on-top of ubuntu Focal"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      app.kubernetes.io/version="${git_version}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN PORTABLE=1 DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared

FROM ghcr.io/oshied/base-build:jammy as jammy
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
ARG name="base-rocksdb"
ARG summary="Base build image for rocksdb built on-top of ubuntu Jammy"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      app.kubernetes.io/version="${git_version}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN PORTABLE=1 DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared
