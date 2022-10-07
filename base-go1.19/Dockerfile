FROM cloudnull/base-build:latest
ARG GO_URL=https://go.dev/dl/go1.19.2.linux-amd64.tar.gz
RUN rm -rf /usr/local/go
RUN curl -L "$GO_URL" -o /tmp/go-linux-amd64.tar.gz
RUN tar -C /usr/local -xzf /tmp/go-linux-amd64.tar.gz
ENV PATH="$PATH:/usr/local/go/bin"
