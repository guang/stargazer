from pyspark import SparkContext
sc = SparkContext()
raw = sc.textFile("/guang/dummy.csv") \
    .map(lambda x: x.split(',')) \
    .cache()

# average duration grouped by map
avg_duration_by_map = raw.map(lambda x: (x[5], int(x[10]))) \
    .reduceByKey(lambda x, y: (x+y)/2).collect()
