FROM ghcr.io/oshied/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/comdex-official/comdex.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
WORKDIR /build_dir/build/libs
RUN cp "$(ldd /build_dir/bin/comdex | awk '/wasm/ {print $3}')" /build_dir/build/libs/ || \
    cp "$(ldd /root/go/bin/comdex | awk '/wasm/ {print $3}')" /build_dir/build/libs/
WORKDIR /build_dir/build/bin
RUN cp /build_dir/bin/comdex /build_dir/build/bin/comdex || \
    cp /root/go/bin/comdex /build_dir/build/bin/comdex

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/comdex-official/comdex.git
ARG git_version=main
ARG name="comdex"
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
COPY --from=BUILD /build_dir/build/bin/comdex /usr/local/bin/comdex
COPY --from=BUILD /build_dir/build/libs /usr/local/lib/comdex
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/comdex/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/comdex
ENTRYPOINT ["/usr/local/bin/comdex"]
