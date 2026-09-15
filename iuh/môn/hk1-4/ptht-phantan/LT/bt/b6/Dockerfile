# Multi-stage build đóng gói CẢ Server VÀ Client trong 1 Image duy nhất
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app

# Copy toàn bộ mã nguồn Java và biên dịch
COPY ChatServer.java ChatClient.java ./
RUN javac -encoding UTF-8 ChatServer.java ChatClient.java

# Runtime Image siêu nhẹ với JRE Alpine
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app

# Copy các file .class đã biên dịch
COPY --from=builder /app/*.class ./
COPY entrypoint.sh ./

# Đảm bảo quyền thực thi và định dạng LF cho script
RUN sed -i 's/\r$//' entrypoint.sh && chmod +x entrypoint.sh

ENV PORT=5000
ENV SERVER_HOST=localhost
ENV SERVER_PORT=5000

EXPOSE 5000

# Entrypoint tự động điều phối: không truyền gì chạy Server, truyền "client" chạy Client
ENTRYPOINT ["/app/entrypoint.sh"]
