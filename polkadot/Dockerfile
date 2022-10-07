FROM cloudnull/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/paritytech/polkadot
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN /root/.cargo/bin/rustup update nightly
RUN /root/.cargo/bin/rustup update stable
RUN /root/.cargo/bin/rustup target add wasm32-unknown-unknown --toolchain nightly
RUN /root/.cargo/bin/cargo +nightly install --git https://github.com/alexcrichton/wasm-gc --force
RUN /root/.cargo/bin/cargo build --release

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/polkadot /usr/local/bin/polkadot
ENTRYPOINT ["/usr/local/bin/polkadot"]
