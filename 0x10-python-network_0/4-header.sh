#!/bin/bash
#  sends a GET request to the URL with header var X-School-User-Id and value 98
curl -sH "X-School-User-Id:98" "$1"
