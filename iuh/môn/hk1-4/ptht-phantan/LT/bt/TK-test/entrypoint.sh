#!/bin/sh

MODE="${1:-server}"

if [ "$MODE" = "client" ]; then
    shift
    exec java AuctionClient "$@"
else
    exec java AuctionServer
fi
