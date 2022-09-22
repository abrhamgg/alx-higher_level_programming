#!/bin/bash
#Bash script that takes URL as argument  sends header Variable
curl -sH "X-School-User-Id: 98" "$1"
