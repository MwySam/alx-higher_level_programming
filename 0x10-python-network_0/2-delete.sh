#!/bin/bash
# send delete request passed as $1
curl -s "$1" -X DELETE
