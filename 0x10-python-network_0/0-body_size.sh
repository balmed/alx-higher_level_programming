#!/bin/bash
# Send a GET request using curl and store the response
curl -so /dev/null -w '%{size_download}\n' $1
