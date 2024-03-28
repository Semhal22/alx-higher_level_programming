#!/bin/bash
# JSON POST request with contents of a file
curl -sX POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
