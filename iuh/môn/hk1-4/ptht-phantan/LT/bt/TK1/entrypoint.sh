#!/bin/sh

if [ "$1" = "client" ] || [ "$1" = "c" ] || [ "$1" = "ChatClient" ]; then
    shift
    exec java ChatClient "$@"
elif [ "$1" = "server" ] || [ "$1" = "s" ] || [ "$1" = "ChatServer" ]; then
    shift
    exec java ChatServer "$@"
elif [ -z "$1" ]; then
    exec java ChatServer
else
    exec "$@"
fi
