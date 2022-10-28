FROM ghcr.io/oshied/base-build:bionic as bionic
ARG name="base-rustup"
ARG summary="Base build image for rust built on-top of ubuntu Bionic"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"

FROM ghcr.io/oshied/base-build:focal as focal
ARG name="base-rustup"
ARG summary="Base build image for rust built on-top of ubuntu Focal"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"

FROM ghcr.io/oshied/base-build:jammy as jammy
ARG name="base-rustup"
ARG summary="Base build image for rust built on-top of ubuntu Jammy"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"
