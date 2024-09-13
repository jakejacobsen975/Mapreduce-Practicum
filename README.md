
# Description

This mapreduce task takes all of the citys temperatures that they have reported for the past 25 years and depending on which task that is chosen it can either give the global or local data. This data consists of the average temperature and, were it is, the count and the min and max temps in the respective place.

## Commands

Because github does not alow transfers of data that are larger then 100 MB here it where I got the data.

https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities?resource=download

To run this version of hadoop state an argument with the command.

```./run.sh```

For example if the user would like to see the min and max temperatures for all cities in this data set simply type the command.

```./run.sh cities```

The command

```./run.sh global```

will only display the global temps.

## Output

To see the output run the command

```cat temperature/part-00000```


