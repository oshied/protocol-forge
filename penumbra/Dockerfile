FROM ghcr.io/oshied/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/penumbra-zone/penumbra
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustup toolchain install 1.60.0-x86_64-unknown-linux-gnu
RUN rustup default 1.60.0-x86_64-unknown-linux-gnu
RUN rustup component add rustfmt
RUN cargo update
RUN cargo build --release --bin pd
RUN cargo build --release --bin pcli

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/penumbra-zone/penumbra
ARG git_version=main
ARG name="penumbra"
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
COPY --from=BUILD /build_dir/target/release/pd /usr/local/bin/pd
COPY --from=BUILD /build_dir/target/release/pcli /usr/local/bin/pcli
ENTRYPOINT ["/usr/local/bin/pcli"]
