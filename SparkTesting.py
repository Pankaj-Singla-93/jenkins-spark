from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('SparkTest')
sc = SparkContext(conf = conf)

#Reading the local text file using SparkContext
testRDD =sc.textFile(r'file:///D:\Fiverr\kw\demo_file.txt',2)

print(type(testRDD))
print(testRDD.collect())
#Pankaj Testing Jenkins
