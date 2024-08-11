#!/bin/bash
# displays method
curl -sI "$1" | grep -i "Allow:" cut -d ' ' -f2-
