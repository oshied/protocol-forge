FROM base-go1.19:latest as BUILD
ARG git_repository=https://github.com/cosmos/gaia.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/gaiad /usr/local/bin/gaiad
ENTRYPOINT ["/usr/local/bin/gaiad"]
