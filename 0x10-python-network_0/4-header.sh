#!/bin/bash
# Sends a GET request with a header variable and value
curl -sH "X-School-User-Id: 98" "$1"
