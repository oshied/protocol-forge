FROM cloudnull/base-build:bionic as bionic
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared

FROM cloudnull/base-build:focal as focal
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared

FROM cloudnull/base-build:jammy as jammy
ENV DEBIAN_FRONTEND="noninteractive"
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt upgrade -y
ARG git_repository=https://github.com/facebook/rocksdb
ARG git_version=main
RUN git clone --recursive --branch $git_version $git_repository /rocksdb
WORKDIR /rocksdb
RUN ln -sf /usr/bin/make /usr/bin/gmake
RUN DISABLE_WARNING_AS_ERROR=1 make -j 16 shared_lib
RUN make install-shared
