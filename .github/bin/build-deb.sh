#!/usr/bin/env bash

export VERSION="${CONTAINER_TAG}"
export DEB_VERSION="${VERSION//[^[:digit:].-]/}"
export BUILD_VERSION="${DEB_VERSION:-0.0.0-$VERSION}"
export BUILD_NAME="$(basename ${PROTOCOL_NAME} | sed 's/.git//g')"
export BUILD_ARCH="$(dpkg --print-architecture)"

sed -i "s/REPLACE_NAME/${BUILD_NAME}/g" /dpgk/DEBIAN/control
sed -i "s/REPLACE_VERSION/${BUILD_VERSION}/g" /dpgk/DEBIAN/control
cp -R /mnt/* /dpgk/
dpkg-deb --build --root-owner-group /dpgk
cp /dpgk.deb "/packages/${BUILD_NAME}_${CONTAINER_TAG}_${BUILD_ARCH}.deb"
