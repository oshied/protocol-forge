FROM ghcr.io/oshied/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/pokt-network/pocket-core
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN go build -o /build_dir/pocket /build_dir/app/cmd/pocket_core/main.go

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/pokt-network/pocket-core
ARG git_version=main
ARG name="pocket"
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
COPY --from=BUILD /build_dir/pocket /usr/local/bin/pocket
ENTRYPOINT ["/usr/local/bin/pocket"]
