#!/bin/bash
# Sends a GET request with a header variable and value
curl -sX GET -H "X-School-User-Id: 98" "$1"
