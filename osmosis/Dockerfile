FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/osmosis-labs/osmosis
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
RUN cp "$(ldd build/osmosisd | awk '/libwasmvm.x86_64.so/ {print $3}')" build/libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/osmosisd /usr/local/bin/osmosisd
COPY --from=BUILD /build_dir/build/chain /usr/local/bin/chain
COPY --from=BUILD /build_dir/build/node /usr/local/bin/node
WORKDIR /usr/local/lib/osmosis
COPY --from=BUILD /build_dir/build/libwasmvm.x86_64.so /usr/local/lib/osmosis/libwasmvm.x86_64.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/osmosis/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/osmosis
ENTRYPOINT ["/usr/local/bin/osmosisd"]
