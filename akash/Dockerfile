FROM cloudnull/base-go1.19:bionic as BUILD
ARG git_repository=https://github.com/ovrclk/akash
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /build_dir
WORKDIR /build_dir
RUN make deps-install
RUN make install

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/bin
COPY --from=BUILD /root/go/bin/akash /usr/local/bin/akash
ENTRYPOINT ["/usr/local/bin/akash"]
