FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/cosmos/cosmos-sdk
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make cosmovisor

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/cosmovisor/cosmovisor /usr/local/bin/cosmovisor
ENTRYPOINT ["/usr/local/bin/cosmovisor"]
