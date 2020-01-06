#!/bin/bash
# Curl a host and print only the dowloaded bytes
curl -s 0.0.0.0:5000 -o null -w "%{size_download}\n"
