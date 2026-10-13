FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app

COPY ChatServer.java ChatClient.java ./
RUN javac -encoding UTF-8 ChatServer.java ChatClient.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app

COPY --from=builder /app/*.class ./
COPY entrypoint.sh ./

RUN sed -i 's/\r$//' entrypoint.sh && chmod +x entrypoint.sh

ENV PORT=5000
ENV SERVER_HOST=localhost
ENV SERVER_PORT=5000

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
