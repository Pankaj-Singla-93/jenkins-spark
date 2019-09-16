from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('SparkTest')
sc = SparkContext(conf = conf)

#Reading the local text file using SparkContext
testRDD =sc.textFile(r'file:///C:\Users\pansingla\Downloads\Fiverr Files\kw\test.txt',2)

print(type(testRDD))
print(testRDD.collect())