#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE="$SCRIPT_DIR/../tests/Test_registration.py"
TEST_FILE2="$SCRIPT_DIR/../tests/test_main_page_deviantart.py"
TEST_FILE3="$SCRIPT_DIR/../tests/Test_Image_count.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE2" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE3" --alluredir="$REPORT_DIR"

