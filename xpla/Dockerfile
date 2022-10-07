FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/xpladev/xpla
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make all
WORKDIR /build_dir/build
RUN cp "$(ldd /root/go/bin/xplad | awk '/libwasmvm.x86_64.so/ {print $3}')" /build_dir/build/libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /root/go/bin/xplad /usr/local/bin/xplad
WORKDIR /usr/local/lib/xpla
COPY --from=BUILD /build_dir/build/libwasmvm.x86_64.so /usr/local/lib/xpla/libwasmvm.x86_64.so
COPY --from=BUILD /lib/x86_64-linux-gnu/libgcc_s.so.1 /usr/local/lib/xpla/libgcc_s.so.1
ENV LD_LIBRARY_PATH=/usr/local/lib/xpla
ENTRYPOINT ["/usr/local/bin/xplad"]
