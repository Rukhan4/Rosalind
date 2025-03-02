#!/bin/bash

# Check if an argument was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <problem_name>"
    exit 1
fi

PROBLEM_DIR="$1"
DATA_DIR="$PROBLEM_DIR/data"
SOLUTION_SCRIPT="$PROBLEM_DIR/solution.py"

# Check if the problem directory exists
if [ ! -d "$PROBLEM_DIR" ]; then
    echo "Error: Directory '$PROBLEM_DIR' not found."
    exit 1
fi

# Check if solution script exists
if [ ! -f "$SOLUTION_SCRIPT" ]; then
    echo "Error: Solution script '$SOLUTION_SCRIPT' not found."
    exit 1
fi

# Ensure the data directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo "Error: Data directory '$DATA_DIR' not found."
    exit 1
fi

# Find the first input file inside the data directory (excluding output.txt)
INPUT_FILE=$(find "$DATA_DIR" -type f ! -name "output.txt" | head -n 1)

# Check if an input file was found
if [ -z "$INPUT_FILE" ]; then
    echo "Error: No input file found in '$DATA_DIR'."
    exit 1
fi

# Define output file name
OUTPUT_FILE="$DATA_DIR/output.txt"

# Run the Python solution with input and output arguments
python3 "$SOLUTION_SCRIPT" "$INPUT_FILE" "$OUTPUT_FILE"

echo "Executed solution script: $SOLUTION_SCRIPT"
echo "Input file: $INPUT_FILE"
echo "Output saved to: $OUTPUT_FILE"
echo " "