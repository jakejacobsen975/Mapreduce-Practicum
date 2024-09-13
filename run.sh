#!/bin/bash

# Define the default reducer
DEFAULT_REDUCER="reducerGlobal.py"

# Check if an argument is provided; the argument can either be global or reducer
if [ "$#" -eq 1 ]; then
    case "$1" in
        global)
            REDUCER="reducerGlobal.py"
            ;;
        cities)
            REDUCER="reducerCities.py"
            ;;
        *)
            echo "Invalid argument. Using default reducerGlobal.py."
            REDUCER="$DEFAULT_REDUCER"
            ;;
    esac
else
    # No argument provided, use the default reducer
    REDUCER="$DEFAULT_REDUCER"
fi

# Define the output directory
OUTPUT_DIR="temperature"

# Check if the output directory exists in HDFS and delete it if it does
echo "Checking if output directory $OUTPUT_DIR exists in HDFS..."
if hadoop fs -test -d $OUTPUT_DIR; then
    echo "Output directory $OUTPUT_DIR exists. Deleting..."
    hadoop fs -rm -r $OUTPUT_DIR
    if [ $? -eq 0 ]; then
        echo "Successfully deleted $OUTPUT_DIR."
    else
        echo "Failed to delete $OUTPUT_DIR."
    fi
else
    echo "Output directory $OUTPUT_DIR does not exist. No need to delete."
fi

# Run the Hadoop streaming job
echo "Running Hadoop streaming job with reducer $REDUCER..."
hadoop jar /home/jake/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
    -mapper mapper.py \
    -reducer $REDUCER \
    -input city_temperature.csv \
    -output $OUTPUT_DIR

if [ $? -eq 0 ]; then
    echo "Hadoop job completed successfully."
else
    echo "Hadoop job failed."
fi
