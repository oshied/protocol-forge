FROM cloudnull/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/paritytech/polkadot
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN /root/.cargo/bin/rustup update nightly
RUN /root/.cargo/bin/rustup update stable
RUN /root/.cargo/bin/rustup target add wasm32-unknown-unknown --toolchain nightly
RUN /root/.cargo/bin/cargo +nightly install --git https://github.com/alexcrichton/wasm-gc --force
RUN /root/.cargo/bin/cargo build --release

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/paritytech/polkadot
ARG git_version=main
ARG name="polkadot"
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
      org.opencontainers.image.vendor="cloudnull.io"
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/polkadot /usr/local/bin/polkadot
ENTRYPOINT ["/usr/local/bin/polkadot"]
