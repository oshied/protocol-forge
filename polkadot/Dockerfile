FROM ghcr.io/oshied/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/paritytech/polkadot
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v21.7/protoc-21.7-linux-x86_64.zip
RUN unzip protoc-21.7-linux-x86_64.zip -d /usr/local
WORKDIR /build_dir
RUN /root/.cargo/bin/rustup update
ENV PATH=$PATH:/root/.cargo/bin
RUN rustup toolchain remove nightly && /build_dir/scripts/init.sh
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
      org.opencontainers.image.url="https://github.com/oshied/protocol-forge" \
      org.opencontainers.image.authors="kevin@cloudnull.com" \
      org.opencontainers.image.revision="${git_version}" \
      org.opencontainers.image.source="${git_repository}" \
      org.opencontainers.image.vendor="cloudnull.io" \
      org.opencontainers.image.description="${summary}"
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/polkadot /usr/local/bin/polkadot
ENTRYPOINT ["/usr/local/bin/polkadot"]
