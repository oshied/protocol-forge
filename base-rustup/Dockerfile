FROM ubuntu:18.04
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update
RUN apt install -y gpg wget curl
RUN curl https://apt.kitware.com/kitware-archive.sh -sSf | sh
RUN apt install -y git clang libssl-dev llvm libudev-dev build-essential cmake pkg-config
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:$HOME/.cargo/bin"
RUN git config --global --add safe.directory '*'
RUN git config --global submodule.recurse true
