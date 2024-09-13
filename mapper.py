#!/bin/python3
import sys

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    parts = line.split(',')
    
    # Ensure the CSV has at least 8 columns and try to parse temperature
    if len(parts) < 8:
        print("Skipping line: not enough columns", file=sys.stderr)
        continue
    
    try:
        # Extract temperature from the last column and city from the fourth column
        temperature = float(parts[-1])
        city = parts[3]  # City is in the fourth column (index 3)
        # Output the city and temperature with a key 'temp'
        print(f"{city}\t{temperature}")
    except ValueError as e:
        print(f"Error processing line: {line}, {e}", file=sys.stderr)
        continue
