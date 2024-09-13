#!/bin/python3
import sys

city_temps = {}

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

    if city not in city_temps:
        city_temps[city] = {'min_temp': temp, 'max_temp': temp, 'sum_temp': temp, 'count': 1}
    else:
        city_temps[city]['sum_temp'] += temp
        city_temps[city]['count'] += 1
        if temp < city_temps[city]['min_temp']:
            city_temps[city]['min_temp'] = temp
        if temp > city_temps[city]['max_temp']:
            city_temps[city]['max_temp'] = temp

# Print results for each city
for city, stats in city_temps.items():
    min_temp = stats['min_temp']
    max_temp = stats['max_temp']
    count = stats['count']
    avg_temp = stats['sum_temp'] / count
    print(f"City: {city}, Min Temperature: {min_temp}, Max Temperature: {max_temp}, Count: {count}, Average Temperature: {avg_temp:.2f}")
