FROM cloudnull/base-rocksdb:focal-v6.29.3 as BUILD_ROCKS

FROM cloudnull/base-go1.19:focal as BUILD_GO

FROM cloudnull/base-nodejs-lts:focal as BUILD
WORKDIR /usr/local/lib
COPY --from=BUILD_ROCKS /usr/local/lib/librocksdb.so /usr/local/lib/
COPY --from=BUILD_ROCKS /usr/local/lib/librocksdb.so.6.29 /usr/local/lib/
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

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/packages/arb-rpc-node/cmd/arb-node/arb-node /usr/local/bin/
WORKDIR /usr/local/lib/arbitrum
COPY --from=BUILD /usr/local/lib/librocksdb.so /usr/local/lib/arbitrum/
COPY --from=BUILD /usr/local/lib/librocksdb.so.6.29 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libgmp.so.10 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libstdc++.so.6 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libatomic.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libsnappy.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libgflags.so.2.2 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libz.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libbz2.so.1.0 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/liblz4.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libzstd.so.1 /usr/local/lib/arbitrum/
COPY --from=BUILD /lib/x86_64-linux-gnu/libnuma.so.1 /usr/local/lib/arbitrum/
ENV LD_LIBRARY_PATH=/usr/local/lib/arbitrum
ENTRYPOINT ["/usr/local/bin/arb-node"]
