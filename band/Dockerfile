FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/bandprotocol/chain
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make install
WORKDIR /build_dir/build
RUN cp /root/go/bin/* /build_dir/build/
RUN cp "$(ldd /build_dir/build/bandd | awk '/libgo_owasm.so/ {print $3}')" /build_dir/build/libgo_owasm.so

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/bandprotocol/chain
ARG git_version=main
ARG name="band"
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
COPY --from=BUILD /build_dir/build/bandd /usr/local/bin/bandd
COPY --from=BUILD /build_dir/build/yoda /usr/local/bin/yoda
WORKDIR /usr/local/lib/band
COPY --from=BUILD /build_dir/build/libgo_owasm.so /usr/local/lib/band/libgo_owasm.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/band/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/band
ENTRYPOINT ["/usr/local/bin/bandd"]
