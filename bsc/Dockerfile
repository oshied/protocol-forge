FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/binance-chain/bsc
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make all

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/binance-chain/bsc
ARG git_version=main
ARG name="bsc"
ARG summary="Distroless container build for ${name}."
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      app.kubernetes.io/version="${git_version}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/cloudnull/protocol-builds" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io"
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/bin/abidump /usr/local/bin/abidump
COPY --from=BUILD /build_dir/build/bin/abigen /usr/local/bin/abigen
COPY --from=BUILD /build_dir/build/bin/bootnode /usr/local/bin/bootnode
COPY --from=BUILD /build_dir/build/bin/checkpoint-admin /usr/local/bin/checkpoint-admin
COPY --from=BUILD /build_dir/build/bin/clef /usr/local/bin/clef
COPY --from=BUILD /build_dir/build/bin/devp2p /usr/local/bin/devp2p
COPY --from=BUILD /build_dir/build/bin/ethkey /usr/local/bin/ethkey
COPY --from=BUILD /build_dir/build/bin/evm /usr/local/bin/evm
COPY --from=BUILD /build_dir/build/bin/faucet /usr/local/bin/faucet
COPY --from=BUILD /build_dir/build/bin/geth /usr/local/bin/geth
COPY --from=BUILD /build_dir/build/bin/p2psim /usr/local/bin/p2psim
COPY --from=BUILD /build_dir/build/bin/puppeth /usr/local/bin/puppeth
COPY --from=BUILD /build_dir/build/bin/rlpdump /usr/local/bin/rlpdump
ENTRYPOINT ["/usr/local/bin/geth"]
