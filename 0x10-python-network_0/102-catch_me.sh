#!/bin/bash
# Curl a host but ignore response and print a message
curl -s -o null -w "You got me!" 0.0.0.0:5000/catch_me
