#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

REPORT_DIR="$SCRIPT_DIR/../tests/results"

allure serve "$REPORT_DIR"