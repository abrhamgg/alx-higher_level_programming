#!/bin/bash
# curl sends GET req to URL, displays response body
echo -n $(curl -sH -X GET "X-School-User-Id: 98" "$1") | echo Hello School!
