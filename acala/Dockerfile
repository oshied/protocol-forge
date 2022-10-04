FROM base-rustup:latest as BUILD
ARG git_repository=https://github.com/AcalaNetwork/Acala
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN export PATH="$PATH:$HOME/.cargo/bin" && make init
RUN export PATH="$PATH:$HOME/.cargo/bin" && make build-release

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/production/acala /usr/local/bin/acala
ENTRYPOINT ["/usr/local/bin/acala"]
