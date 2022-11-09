FROM ghcr.io/oshied/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/ovrclk/akash
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
# NOTE: work around until https://github.com/ovrclk/akash/pull/1714 is merged
RUN sed -i 's@"$(AKASH_DEVCACHE_BIN):$(AKASH_DEVCACHE_NODE_BIN):$(PATH)"@$(AKASH_DEVCACHE_BIN):$(AKASH_DEVCACHE_NODE_BIN):$(PATH)@' make/init.mk
RUN make deps-install
RUN make install

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/ovrclk/akash
ARG git_version=main
ARG name="akash"
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
COPY --from=BUILD /root/go/bin/akash /usr/local/bin/akash
ENTRYPOINT ["/usr/local/bin/akash"]
