FROM cloudnull/base-go1.19:focal as BUILD
ARG git_repository=https://github.com/aptos-labs/aptos-core
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN echo y | ./scripts/dev_setup.sh
RUN /root/.cargo/bin/cargo build -p aptos-node --release

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/aptos-node /usr/local/bin/aptos-node
ENTRYPOINT ["/usr/local/bin/aptos-node"]
