#!/bin/bash
#script tht shows the size of HTTP response body
curl -s -I $1 | grep -i Content-Length | awk '{print $2}'
