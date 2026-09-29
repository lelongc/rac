FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /build
COPY . /build
RUN javac -encoding UTF-8 *.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /build/*.class /app/
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENV RMI_PORT=1099
ENV SOCKET_PORT=5000
ENV RMI_HOST=localhost
ENV SERVER_HOST=localhost

EXPOSE 1099 5000
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["server"]
