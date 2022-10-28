FROM ghcr.io/oshied/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/centrifuge/centrifuge-chain
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN /build_dir/scripts/init.sh
RUN /root/.cargo/bin/cargo build --release

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/centrifuge/centrifuge-chain
ARG git_version=main
ARG name="centrifuge"
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
COPY --from=BUILD /build_dir/target/release/centrifuge-chain /usr/local/bin/centrifuge-chain
WORKDIR /usr/local/lib/centrifuge
COPY --from=BUILD /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/local/lib/centrifuge/libstdc++.so.6
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/centrifuge/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/centrifuge
ENTRYPOINT ["/usr/local/bin/centrifuge-chain"]
