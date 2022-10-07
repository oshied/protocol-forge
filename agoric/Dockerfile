FROM cloudnull/base-go1.19:latest as GO_BUILD

FROM cloudnull/base-nodejs-lts:latest as BUILD
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
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/packages/cosmic-swingset/bin/ag-chain-cosmos /usr/local/bin/ag-chain-cosmos
COPY --from=BUILD /build_dir/packages/cosmic-swingset/bin/ag-nchainz /usr/local/bin/ag-nchainz
COPY --from=BUILD /build_dir/packages/cosmic-swingset/src /usr/local/src
CMD ["/usr/local/src/entrypoint.js"]
