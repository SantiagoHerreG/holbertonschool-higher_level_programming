#!/bin/bash
# Curl a host with GET request, and header setting
curl -sL "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
