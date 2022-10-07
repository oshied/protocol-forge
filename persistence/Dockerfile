FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/persistenceOne/persistenceCore
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/persistenceCore /usr/local/bin/persistenceCore
ENTRYPOINT ["/usr/local/bin/persistenceCore"]
