#!/bin/bash
# POST request with message and display response body
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1
