#!/bin/bash
# sends a json file using POST reuest
curl -s -X POST -H 'Content-Type:application/json' -d @$2 $1
