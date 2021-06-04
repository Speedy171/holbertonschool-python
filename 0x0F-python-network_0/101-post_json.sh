#!/bin/bash
# Sends JSON POST request and display its body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
