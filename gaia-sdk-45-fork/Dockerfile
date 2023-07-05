FROM ghcr.io/oshied/base-go1.18:jammy as BUILD
ARG git_repository=https://github.com/cosmos/gaia.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN sed -i 's@github.com/cosmos/cosmos-sdk =>.*@github.com/cosmos/cosmos-sdk => github.com/notional-labs/cosmos-sdk v0.45.16-0.20230409050322-1846175439ec@' go.mod
RUN sed -i 's@github.com/cosmos/cosmos-sdk v0.45.16-ics h1.*@github.com/notional-labs/cosmos-sdk v0.45.16-0.20230409050322-1846175439ec h1:tLRNo92hab2C+sF4GKPeP45K8ZlizcQ0WeX2NC0Kb9k=@' go.sum
RUN sed -i 's@github.com/cosmos/cosmos-sdk v0.45.16-ics/go.mod h1.*@github.com/notional-labs/cosmos-sdk v0.45.16-0.20230409050322-1846175439ec/go.mod h1:bScuNwWAP0TZJpUf+SHXRU3xGoUPp+X9nAzfeIXts40=@' go.sum
RUN make build

FROM gcr.io/distroless/base-debian11:latest
ARG git_repository=https://github.com/cosmos/gaia.git
ARG git_version=main
ARG name="gaia-sdk-45-fork"
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
COPY --from=BUILD /build_dir/build/gaiad /usr/local/bin/gaia-sdk-45-fork
ENTRYPOINT ["/usr/local/bin/gaia-sdk-45-fork"]
