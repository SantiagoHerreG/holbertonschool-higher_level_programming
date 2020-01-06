#!/bin/bash
# Curl a host header only and cut desired fields
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2,3,4,5,6,7,8,9,10
