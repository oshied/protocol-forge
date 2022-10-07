FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/althea-net/althea-chain
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN go get github.com/althea-net/cosmos-gravity-bridge/module@$git_version
RUN make build

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/althea /usr/local/bin/althea
ENTRYPOINT ["/usr/local/bin/althea"]
