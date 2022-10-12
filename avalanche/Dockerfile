FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/ava-labs/avalanchego
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN ./scripts/build.sh

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/avalanchego /usr/local/bin/avalanchego
COPY --from=BUILD /build_dir/build/plugins /usr/local/bin/plugins
ENTRYPOINT ["/usr/local/bin/avalanchego"]
