#!/bin/sh

# Nếu tham số đầu là "client" hoặc "c" -> chạy ChatClient
if [ "$1" = "client" ] || [ "$1" = "c" ] || [ "$1" = "ChatClient" ]; then
    shift
    exec java ChatClient "$@"
# Nếu tham số đầu là "server" hoặc "s" -> chạy ChatServer
elif [ "$1" = "server" ] || [ "$1" = "s" ] || [ "$1" = "ChatServer" ]; then
    shift
    exec java ChatServer "$@"
# Mặc định không truyền tham số -> chạy ChatServer
elif [ -z "$1" ]; then
    exec java ChatServer
# Nếu truyền lệnh tùy biến khác
else
    exec "$@"
fi
