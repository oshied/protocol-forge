FROM cloudnull/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/MystenLabs/sui
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
ENV PATH="$PATH:$HOME/.cargo/bin"
RUN /root/.cargo/bin/rustup toolchain install 1.62.1-x86_64-unknown-linux-gnu
RUN /root/.cargo/bin/rustup default 1.62.1-x86_64-unknown-linux-gnu
RUN /root/.cargo/bin/rustup component add rustfmt
RUN /root/.cargo/bin/cargo build --release --bin sui-node
RUN /root/.cargo/bin/cargo build --release --bin sui

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/MystenLabs/sui
ARG git_version=main
ARG name="sui"
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
COPY --from=BUILD /build_dir/target/release/sui /usr/local/bin/sui
COPY --from=BUILD /build_dir/target/release/sui-node /usr/local/bin/sui-node
ENTRYPOINT ["/usr/local/bin/sui"]
