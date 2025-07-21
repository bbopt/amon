#!/bin/bash

PROGRAM="amon run 2 AMON_HOME/starting_pts/x2.txt -f "
ARGS=("1" "0.9" "0.8" "0.7" "0.6" "0.5" "0.4" "0.3" "0.2" "0.1" "0")

for arg in "${ARGS[@]}"; do
    echo "Running: $PROGRAM $arg"
    start_time=$(date +%s)

    $PROGRAM "$arg"

    end_time=$(date +%s)
    elapsed=$((end_time - start_time))
    echo "Time taken: ${elapsed}s"
    echo
done

