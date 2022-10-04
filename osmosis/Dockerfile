FROM cloudnull/base-go1.19:latest as BUILD
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
ENV LD_LIBRARY_PATH=/usr/local/lib/osmosis/libwasmvm.x86_64.so
ENTRYPOINT ["/usr/local/bin/osmosisd"]
