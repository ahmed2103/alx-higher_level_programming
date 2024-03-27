#!/bin/bash
#Bash script that takes in a URL and 
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ {print $2 }'
