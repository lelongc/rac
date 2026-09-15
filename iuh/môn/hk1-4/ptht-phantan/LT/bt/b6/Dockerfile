# Mặc định Dockerfile đóng gói ChatServer
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY ChatServer.java .
COPY ChatClient.java .
RUN javac -encoding UTF-8 ChatServer.java ChatClient.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/*.class .

ENV PORT=5000
EXPOSE 5000

CMD ["java", "ChatServer"]
