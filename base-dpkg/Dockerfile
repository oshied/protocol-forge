FROM ghcr.io/oshied/base-build:bionic as bionic
ARG name="base-dpkg"
ARG summary="DPKG build environment"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN apt install -y dpkg gettext-base
WORKDIR /dpgk/DEBIAN
COPY debian/control /dpgk/DEBIAN/control
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postinst
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postrm
WORKDIR /packages

FROM ghcr.io/oshied/base-build:focal as focal
ARG name="base-dpkg"
ARG summary="DPKG build environment"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN apt install -y dpkg gettext-base
WORKDIR /dpgk/DEBIAN
COPY debian/control /dpgk/DEBIAN/control
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postinst
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postrm
WORKDIR /packages

FROM ghcr.io/oshied/base-build:jammy as jammy
ARG name="base-dpkg"
ARG summary="DPKG build environment"
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
RUN apt install -y dpkg gettext-base
WORKDIR /dpgk/DEBIAN
COPY debian/control /dpgk/DEBIAN/control
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postinst
COPY --chmod=0755 debian/postinst /dpgk/DEBIAN/postrm
WORKDIR /packages
