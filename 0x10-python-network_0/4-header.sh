#!/bin/bash
# curl sends GET req to URL, displays response body
echo -n $(curl -s -H "X-School-User-Id: 98" "$1")
