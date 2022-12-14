FROM ghcr.io/oshied/base-rocksdb:focal-v6.29.3 as BUILD_ROCKS

FROM ghcr.io/oshied/base-go1.19:focal as BUILD_GO

FROM ghcr.io/oshied/base-nodejs-lts:focal as BUILD
WORKDIR /usr/local/lib
COPY --from=BUILD_ROCKS /usr/local/lib /usr/local/lib
WORKDIR /usr/local/include
COPY --from=BUILD_ROCKS /usr/local/include/rocksdb /usr/local/include/rocksdb
WORKDIR /usr/local/bin
COPY --from=BUILD_GO /usr/local/go /usr/local/go
ARG git_repository=https://github.com/OffchainLabs/arbitrum
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN ln -sf /usr/bin/make /usr/bin/gmake
WORKDIR /build_dir/packages/arb-avm-cpp/release
ENV LD_LIBRARY_PATH=/usr/local/lib

# Delete me later
RUN apt install -y libusb-dev libusb-1.0-0-dev

RUN cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER='/usr/bin/gcc-9' -DCMAKE_CXX_COMPILER='/usr/bin/g++-9' -DCMAKE_BUILD_TYPE='Release'
RUN cmake --build .
WORKDIR /build_dir/packages/arb-rpc-node/cmd/arb-node
RUN /usr/local/go/bin/go build ./
WORKDIR /build_dir/packages/arb-avm-cpp/release/lib
RUN cp /usr/local/lib/librocksdb* \
       /lib/x86_64-linux-gnu/libgmp* \
       /lib/x86_64-linux-gnu/libstdc* \
       /lib/x86_64-linux-gnu/libatomic* \
       /lib/x86_64-linux-gnu/libgcc_s* \
       /lib/x86_64-linux-gnu/libsnappy* \
       /lib/x86_64-linux-gnu/libgflags* \
       /lib/x86_64-linux-gnu/libz* \
       /lib/x86_64-linux-gnu/libbz2* \
       /lib/x86_64-linux-gnu/liblz4* \
       /lib/x86_64-linux-gnu/libzstd* \
       /lib/x86_64-linux-gnu/libnuma* /build_dir/packages/arb-avm-cpp/release/lib/

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/OffchainLabs/arbitrum
ARG git_version=main
ARG name="arbitrum"
ARG summary="Distroless container build for ${name}."
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
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/packages/arb-rpc-node/cmd/arb-node/arb-node /usr/local/bin/arb-node
WORKDIR /usr/local/lib/arbitrum
COPY --from=BUILD /build_dir/packages/arb-avm-cpp/release/lib /usr/local/lib/arbitrum
ENV LD_LIBRARY_PATH=/usr/local/lib/arbitrum
ENTRYPOINT ["/usr/local/bin/arb-node"]
