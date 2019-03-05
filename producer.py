from kafka import KafkaProducer
from kafka.errors import KafkaError
from metrics import Metrics

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'defender_agent'

class Producer(object):

    def __init__(self):
        pass
    
    #metrics need to json data
    def send(self, metrics):
        #print (metrics)
        producer.send('defender_agent', metrics.encode('utf-8'))
        producer.flush()
