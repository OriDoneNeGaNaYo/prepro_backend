from kafka import KafkaConsumer, KafkaProducer

# 추천 알고리즘 
from pyspark.mllib.recommendation import ALS
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler



broker = ["localhost:9091", "localhost:9092", "localhost:9093"]

topic_name = "~~"
consumer = KafkaConsumer(topic_name, bootstrap_servers=broker)
producer = KafkaProducer(bootstrap_servers=broker)


def spark_preprocessing():
    pass


def recommendation():
    pass

