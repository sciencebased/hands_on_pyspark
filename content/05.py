# Boiler plate stuff
from pyspark import SparkConf, SparkContext
import collections

#SparkConf= Helps me to configure context
#collections= From python

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
'''
#conf= master node as local machine, in this 
#sc SparkContext
'''
lines = sc.textFile("ml-100k/u.data")
'''
This instructions reads the file and creates an RDD called lines.
'''
ratings = lines.map(lambda x: x.split()[2])
'''
This instruction maps each line to its third element (rating).
'''
result = ratings.countByValue()
#obvious, this instruction counts the number of occurrences of each rating value.
print("This is result", result)
sortedResults = collections.OrderedDict(sorted(result.items()))
#sorted in descending order, and then creates an ordered dictionary to maintain the order of the results.
for key, value in sortedResults.items():
    print(f"{key}: {value}")