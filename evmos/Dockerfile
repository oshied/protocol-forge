FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/evmos/evmos.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN go mod download github.com/miguelmota/go-ethereum-hdwallet
RUN make build

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/evmosd /usr/local/bin/evmosd
ENTRYPOINT ["/usr/local/bin/evmosd"]
