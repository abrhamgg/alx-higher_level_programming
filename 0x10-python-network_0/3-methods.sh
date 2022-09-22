#!/bin/bash
#script that lists available HTTP methdos in the server
curl -sI youtube | grep -i Allow | awk "{print $2}"
