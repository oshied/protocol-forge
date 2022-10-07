FROM cloudnull/base-build:bionic as bionic
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"

FROM cloudnull/base-build:focal as focal
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"

FROM cloudnull/base-build:jammy as jammy
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"
