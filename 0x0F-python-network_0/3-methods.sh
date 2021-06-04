#!/bin/bash
# Get allowed methods
curl -sI "$1" | grep Allow | cut -f2- -d " "
