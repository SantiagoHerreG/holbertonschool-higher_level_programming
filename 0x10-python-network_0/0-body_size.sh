#!/bin/bash
# Curl a domain (host) and prints the length of the response
curl -s "$1" -o /dev/null -w "%{size_download}\n"
