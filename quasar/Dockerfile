FROM cloudnull/base-go1.19:latest as BUILD
ARG git_repository=https://github.com/quasar-finance/quasar
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make build
RUN cp "$(ldd build/quasarnoded | awk '/libwasmvm.x86_64.so/ {print $3}')" build/libwasmvm.x86_64.so

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /build_dir/build/quasarnoded /usr/local/bin/quasarnoded
WORKDIR /usr/local/lib/quasar
COPY --from=BUILD /build_dir/build/libwasmvm.x86_64.so /usr/local/lib/quasar/libwasmvm.x86_64.so
ENV LD_LIBRARY_PATH=/usr/local/lib/quasar/libwasmvm.x86_64.so
ENTRYPOINT ["/usr/local/bin/quasarnoded"]
