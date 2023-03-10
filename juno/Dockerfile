FROM ghcr.io/oshied/base-go1.19:focal as BUILD
ARG git_repository=https://github.com/CosmosContracts/juno.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
RUN cp "$(ldd bin/junod | awk '/libwasmvm.x86_64.so/ {print $3}')" libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/CosmosContracts/juno.git
ARG git_version=main
ARG name="juno"
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
COPY --from=BUILD /build_dir/bin/junod /usr/local/bin/junod
WORKDIR /usr/local/lib/juno
COPY --from=BUILD /build_dir/libwasmvm.x86_64.so /usr/local/lib/juno/libwasmvm.x86_64.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/juno/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/juno
ENTRYPOINT ["/usr/local/bin/junod"]
