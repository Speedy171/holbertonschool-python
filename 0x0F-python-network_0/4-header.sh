#!/bin/bash
# Send custom header
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id: 98"
