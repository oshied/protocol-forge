FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/pokt-network/pocket-core
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN go build -o /build_dir/pocket /build_dir/app/cmd/pocket_core/main.go

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/pocket /usr/local/bin/pocket
ENTRYPOINT ["/usr/local/bin/pocket"]
