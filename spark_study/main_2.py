from pyspark.mllib.feature import Word2Vec
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf().setAppName("Montecarlo_PI")
sc = SparkContext(conf=conf)

input = sc.textFile("./files/username.csv").map(lambda row: row.split(" "))

word2vec = Word2Vec()
model = word2vec.fit(input)

name = model.findSynonyms('booker12', 40)

for word, Username in name:
    print(f"{word}: {Username}")