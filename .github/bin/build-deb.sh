#!/usr/bin/env bash

export VERSION="${CONTAINER_TAG}"
export DEB_VERSION="${VERSION//[^[:digit:].]/}"
if [[ $DEB_VERSION =~ ^[[:digit:]] ]]; then
  export BUILD_VERSION="${DEB_VERSION}"
else
  export BUILD_VERSION="0-${VERSION}"
fi
export BUILD_NAME="$(basename ${PROTOCOL_NAME} | sed 's/.git//g')"
export BUILD_ARCH="$(dpkg --print-architecture)"
export BUILD_MAINTAINER="${BUILD_MAINTAINER:-'Kevin Carter <kevin@cloudnull.com>'}"
export BUILD_EXEC="${BUILD_EXEC:-}"

mkdir -p /mnt/DEBIAN
for item in control postinst postrm; do
  envsubst < "/dpgk/DEBIAN/${item}" > "/mnt/DEBIAN/${item}"
done

chmod +x /mnt/DEBIAN/postinst
chmod +x /mnt/DEBIAN/postrm

dpkg-deb --build --root-owner-group /mnt
cp /mnt.deb "/packages/${BUILD_NAME}_${CONTAINER_TAG}_${BUILD_ARCH}.deb"
