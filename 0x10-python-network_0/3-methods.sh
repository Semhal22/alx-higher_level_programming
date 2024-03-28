#!/bin/bash
# Displays all HTTP methods the server accepts
curl -sI "$1" | grep -i '^Allow:' | awk -F': ' '{print $2}'
