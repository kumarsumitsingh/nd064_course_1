FROM golang:alpine

WORKDIR /go/src/ap

ADD . .

RUN go mod init && go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]

