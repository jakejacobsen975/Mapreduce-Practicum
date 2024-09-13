#!/bin/python3
import sys

global_min_temp = float('inf')
global_max_temp = float('-inf')
global_sum_temp = 0.0
global_count = 0

min_temp_city = None
max_temp_city = None

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        city, temp = line.split('\t')
        temp = float(temp)

        if temp == -99:
            continue
    except ValueError:
        print(f"Error processing line: {line}", file=sys.stderr)
        continue

    # Update global statistics
    if temp < global_min_temp:
        global_min_temp = temp
        min_temp_city = city
    if temp > global_max_temp and temp > -98:
        global_max_temp = temp
        max_temp_city = city
    global_sum_temp += temp
    global_count += 1

# Calculate average temperature
if global_count > 0:
    global_avg_temp = global_sum_temp / global_count
else:
    global_avg_temp = 0.0

# Print global statistics with city information
print(f"Global Min Temperature: {global_min_temp} (from {min_temp_city})")
print(f"Global Max Temperature: {global_max_temp} (from {max_temp_city})")
print(f"Global Count: {global_count}")
print(f"Global Average Temperature: {global_avg_temp:.2f}")
