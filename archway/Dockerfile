FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/archway-network/archway
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
RUN cp "$(ldd build/archwayd | awk '/libwasmvm/ {print $3}')" build/libwasmvm.so

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/archwayd /usr/local/bin/archwayd
WORKDIR /usr/local/lib/archway
COPY --from=BUILD /build_dir/build/libwasmvm.so /usr/local/lib/archway/libwasmvm.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/archway/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/archway
ENTRYPOINT ["/usr/local/bin/archwayd"]
