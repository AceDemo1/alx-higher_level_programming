#!/bin/bash
# httpstatuscode
curl -s -o /dev/null -w "%{http_status}" "$1"
