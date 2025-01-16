#!/bin/bash

DIR=$(dirname "$0")

FILE="$DIR/../tests/locustfile.py"

start http://localhost:8089

locust -f "$FILE" --host https://ru.pinterest.com --run-time 10 --autostart --autoquit 10
