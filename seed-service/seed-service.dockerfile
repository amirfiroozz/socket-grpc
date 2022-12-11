# base go image
# FROM golang:1.18-alpine as builder

# RUN mkdir /app

# COPY . /app

# WORKDIR /app

# RUN go mod tidy

# RUN CGO_ENABLED=0 go build -o seedApp ./cmd

# RUN chmod +x /app/seedApp

# # build a tiny docker image
# FROM alpine:latest

# RUN mkdir /app

# COPY --from=builder /app/seedApp /app

# CMD [ "/app/seedApp" ]


FROM alpine:latest

RUN mkdir /app

COPY seedApp /app

CMD ["/app/seedApp"]