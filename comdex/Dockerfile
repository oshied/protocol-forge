FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/comdex-official/comdex.git
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
WORKDIR /build_dir/build
RUN cp "$(ldd /build_dir/bin/comdex | awk '/libwasmvm.x86_64.so/ {print $3}')" /build_dir/build/libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/bin/comdex /usr/local/bin/comdex
WORKDIR /usr/local/lib/comdex
COPY --from=BUILD /build_dir/build/libwasmvm.x86_64.so /usr/local/lib/comdex/libwasmvm.x86_64.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/comdex/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/comdex
ENTRYPOINT ["/usr/local/bin/comdex"]
