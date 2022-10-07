FROM cloudnull/base-rustup:bionic as BUILD
ARG git_repository=https://github.com/near/nearcore
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
ENV PATH="/root/.cargo/bin:${PATH}"
RUN make neard

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/target/release/neard /usr/local/bin/neard
ENTRYPOINT ["/usr/local/bin/neard"]
