#!/bin/bash
#script that lists available HTTP methdos in the server
curl -sI $1 | grep -i Allow | awk "{print $2}"
