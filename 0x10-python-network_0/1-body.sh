#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
url=$1
curl curl -sL $url
