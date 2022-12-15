#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -L -s -X HEAD -w "%{http_code}" "$1"
