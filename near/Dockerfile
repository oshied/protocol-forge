FROM cloudnull/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/near/nearcore
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
ENV PATH="/root/.cargo/bin:${PATH}"
RUN make neard

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/near/nearcore
ARG git_version=main
ARG name="near"
ARG summary="Distroless container build for ${name}."
LABEL description="${summary}" \
      maintainer="cloudnull.io <kevin@cloudnull.com>" \
      app.kubernetes.io/name="${name}" \
      app.kubernetes.io/version="${git_version}" \
      org.opencontainers.image.title="${name}" \
      org.opencontainers.artifact.description="${summary}" \
      org.opencontainers.image.url="https://github.com/cloudnull/protocol-builds" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/neard /usr/local/bin/neard
ENTRYPOINT ["/usr/local/bin/neard"]
