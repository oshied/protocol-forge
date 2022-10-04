FROM cloudnull/base-rustup:latest as BUILD
ARG git_repository=https://github.com/MystenLabs/sui
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
ENV PATH="$PATH:$HOME/.cargo/bin"
RUN /root/.cargo/bin/rustup toolchain install 1.62.1-x86_64-unknown-linux-gnu
RUN /root/.cargo/bin/rustup default 1.62.1-x86_64-unknown-linux-gnu
RUN /root/.cargo/bin/rustup component add rustfmt
RUN /root/.cargo/bin/cargo build --release --bin sui-node
RUN /root/.cargo/bin/cargo build --release --bin sui

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/sui /usr/local/bin/sui
COPY --from=BUILD /build_dir/target/release/sui-node /usr/local/bin/sui-node
ENTRYPOINT ["/usr/local/bin/sui"]
