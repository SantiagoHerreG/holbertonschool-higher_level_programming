#!/bin/bash
# Curl a host but ignore response and print a message
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
