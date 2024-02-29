#!/bin/bash
# sends a req to a URL and displays size of response
url=$1
curl -so /dev/null -w '%{size_download}\n' $url
