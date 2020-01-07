#!/bin/bash
# Curl a host with POST request of a JSON from a file
curl -s -X POST "$1" -H "Content-Type: application/json" -d "$(cat "$2")"
