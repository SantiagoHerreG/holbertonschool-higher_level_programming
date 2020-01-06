#!/bin/bash
# Curl a host and print only the dowloaded bytes
curl -s "$1" | wc -c
