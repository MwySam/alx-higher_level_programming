#!/bin/bash
# send a GET request to the URL, displays the body of the response
curl -sfL "$1" -X GET
