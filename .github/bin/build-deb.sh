#!/usr/bin/env bash

export VERSION="${CONTAINER_TAG}"
export DEB_VERSION="${VERSION//[^[:digit:].-]/}"
export BUILD_VERSION="${DEB_VERSION:-0.0.0-$VERSION}"
export BUILD_NAME="$(basename ${PROTOCOL_NAME} | sed 's/.git//g')"
export BUILD_ARCH="$(dpkg --print-architecture)"

mkdir /mnt/DEBIAN
for item in control postinst postrm; do
  sed -e "s/REPLACE_NAME/${BUILD_NAME}/g" -e "s/REPLACE_VERSION/${BUILD_VERSION}/g" "/dpgk/DEBIAN/${item}" > "/mnt/DEBIAN/${item}"
done

chmod +x /mnt/DEBIAN/postinst
chmod +x /mnt/DEBIAN/postrm

dpkg-deb --build --root-owner-group /mnt
cp /mnt.deb "/packages/${BUILD_NAME}_${CONTAINER_TAG}_${BUILD_ARCH}.deb"
