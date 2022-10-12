FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/quasar-finance/quasar
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
RUN cp "$(ldd build/quasarnoded | awk '/libwasmvm.x86_64.so/ {print $3}')" build/libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/quasar-finance/quasar
ARG git_version=main
ARG name="quasar"
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
COPY --from=BUILD /build_dir/build/quasarnoded /usr/local/bin/quasarnoded
WORKDIR /usr/local/lib/quasar
COPY --from=BUILD /build_dir/build/libwasmvm.x86_64.so /usr/local/lib/quasar/libwasmvm.x86_64.so
ENV LD_LIBRARY_PATH=/usr/local/lib/quasar
ENTRYPOINT ["/usr/local/bin/quasarnoded"]
