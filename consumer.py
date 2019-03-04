from kafka import KafkaConsumer
consumer = KafkaConsumer('defender_agent', bootstrap_servers=['localhost:9092'])
print (consumer)
for message in consumer:
    print (message)
