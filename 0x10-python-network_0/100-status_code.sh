#!/bin/bash
# Curl a host with GET request, print code response using -w
curl -s -o null -w "%{http_code}" "$1"
