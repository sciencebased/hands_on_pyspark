from pyspark import SparkConf, SparkContext
# Boiler plate


conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
#Config master node, this pc
sc = SparkContext(conf = conf)
#Initialize spark context

def parseLine(line):
    #function that recieves line (list)
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])
    #return a list of int (age, numFriends)
    return (age, numFriends)

lines = sc.textFile("/Users/joan.estrada/Desktop/studies/hands_on_pyspark/activities/01/fakefriends.csv")
#convert the textFile into rdd
rdd = lines.map(parseLine)
#convert the rdd into another after passing for a custom function
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
#lambda x: (x,1) => input: (age, numFriends), output (age, (numFriends, 1))
#lambda x, y: (x[0] + y[0], x[1] + y[1]) 
#   => input {(age, (numFriends, 1)), (age2, (numFriends2,1))} 
#   => output {age, (numFriends+numFriends2, 2)}
#   ....
averagesByAge = totalsByAge.mapValues(lambda x: int(x[0] / x[1]))
results = averagesByAge.collect()
for result in results:
    print(result)
