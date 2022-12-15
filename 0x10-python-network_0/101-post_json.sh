#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
