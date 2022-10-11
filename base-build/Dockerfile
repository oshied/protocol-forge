FROM ubuntu:18.04 as bionic
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt install -y gpg wget curl git software-properties-common
RUN git config --global --add safe.directory '*'
RUN git config --global submodule.recurse true
RUN curl https://apt.kitware.com/kitware-archive.sh -sSf | sh
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt install -y git build-essential libssl-dev libgmp3-dev libboost-all-dev libsnappy-dev \
                                 libzstd-dev llvm libudev-dev software-properties-common python3-dev gcc-9 \
                                 g++-9 make cmake clang clang-format autoconf automake libgflags-dev \
                                 zlib1g-dev libbz2-dev liblz4-dev libtool pkg-config sudo apt-utils libusb-dev

FROM ubuntu:20.04 as focal
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt install -y gpg wget curl git software-properties-common
RUN git config --global --add safe.directory '*'
RUN git config --global submodule.recurse true
RUN curl https://apt.kitware.com/kitware-archive.sh -sSf | sh
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt update && apt install -y git build-essential libssl-dev libgmp3-dev libboost-all-dev libsnappy-dev \
                                 libzstd-dev llvm libudev-dev software-properties-common python3-dev gcc-9 \
                                 g++-9 make cmake clang clang-format autoconf automake libgflags-dev \
                                 zlib1g-dev libbz2-dev liblz4-dev libtool pkg-config sudo apt-utils libusb-dev

FROM ubuntu:22.04 as jammy
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt install -y gpg wget curl git software-properties-common
RUN git config --global --add safe.directory '*'
RUN git config --global submodule.recurse true
RUN apt update && apt install -y git build-essential libssl-dev libgmp3-dev libboost-all-dev libsnappy-dev \
                                 libzstd-dev llvm libudev-dev software-properties-common python3-dev gcc-9 \
                                 g++-9 make cmake clang clang-format autoconf automake libgflags-dev \
                                 zlib1g-dev libbz2-dev liblz4-dev libtool pkg-config sudo apt-utils libusb-dev
