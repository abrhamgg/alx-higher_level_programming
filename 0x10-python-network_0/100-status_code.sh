#!/bin/bash
#script tha displays only the status code
curl -s -o dev/null $1 -w %{http_code}
