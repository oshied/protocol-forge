FROM cloudnull/base-build:jammy as BUILD
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN DISABLE_WARNING_AS_ERROR=1 make -j 16 static_lib
RUN make install-static

FROM gcr.io/distroless/base-debian11:latest
WORKDIR /usr/local/lib
COPY --from=BUILD /usr/local/lib/librocksdb.a /usr/local/lib/librocksdb.a
WORKDIR /usr/local/lib/pkgconfig
COPY --from=BUILD /usr/local/lib/pkgconfig/rocksdb.pc /usr/local/lib/pkgconfig/rocksdb.pc
