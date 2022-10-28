FROM ghcr.io/oshied/base-go1.19:bionic as GO_BUILD

FROM ghcr.io/oshied/base-nodejs-lts:bionic as BUILD
ARG git_repository=https://github.com/Agoric/agoric-sdk
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN yarn
RUN yarn build
COPY --from=GO_BUILD /usr/local/go /usr/local/go
ENV PATH="$PATH:/usr/local/go/bin"
WORKDIR /build_dir/packages/cosmic-swingset
RUN make all

FROM gcr.io/distroless/nodejs:16
ARG git_repository=https://github.com/Agoric/agoric-sdk
ARG git_version=main
ARG name="agoric"
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
COPY --from=BUILD /build_dir/packages/cosmic-swingset/bin/ag-chain-cosmos /usr/local/bin/ag-chain-cosmos
COPY --from=BUILD /build_dir/packages/cosmic-swingset/bin/ag-nchainz /usr/local/bin/ag-nchainz
COPY --from=BUILD /build_dir/packages/cosmic-swingset/src /usr/local/src
CMD ["/usr/local/src/entrypoint.js"]
