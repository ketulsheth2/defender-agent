from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('defender_agent', bootstrap_servers=['localhost:9092'])
print (consumer)
for message in consumer:
    m = json.loads((message.value).decode('utf-8'))
    print (m)
