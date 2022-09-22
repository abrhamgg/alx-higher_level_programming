#!/bin/bash
# curl sends GET req to URL, displays response body
echo -n $(curl -sH -i "X-School-User-Id: 98" "$1")
