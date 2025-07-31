#!/bin/bash

# Use GNU date (gdate) for millisecond precision
DATE_CMD="date"

PROGRAM="amon run 1 AMON_HOME/starting_pts/x1.txt -s 1 -f"
ARGS=("1" "0.9" "0.8" "0.7" "0.6" "0.5" "0.4" "0.3" "0.2" "0.1" "0")

for arg in "${ARGS[@]}"; do
    echo "Running: $PROGRAM $arg"

    start_time=$($DATE_CMD +%s)

    $PROGRAM "$arg"

    end_time=$($DATE_CMD +%s)
    elapsed_ms=$((end_time - start_time))
    elapsed_sec=$(awk "BEGIN {printf \"%.3f\", $elapsed_ms / 1000}")

    echo "Time taken: ${elapsed_sec}s"
    echo
done
