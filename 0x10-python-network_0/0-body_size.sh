#!/bin/bash
# Sends request to a URL and displays size of body of response
curl -sI "$1" | grep -i '^Content-length:' | awk '{print $2}'
