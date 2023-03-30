#!/bin/bash
# displays only the status code of the response.
curl -o /dev/null -w '%{http_code}' -sLI "$1"
