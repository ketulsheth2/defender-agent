from kafka import KafkaConsumer
import json
import csv

row = ['listening_tcp_ports', 'listening_udp_ports', 'tcp_connections']

with open('sample_data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows([row])
writeFile.close()

consumer = KafkaConsumer('defender_agent', bootstrap_servers=['localhost:9092'])
print (consumer)
for message in consumer:
    data = json.loads((message.value).decode('utf-8'))
    listdata = list()
    listdata.append(data['metrics']['listening_tcp_ports']['total'])
    listdata.append(data['metrics']['listening_udp_ports']['total'])
    listdata.append(data['metrics']['tcp_connections']['established_connections']['total'])
    print (listdata)
    with open('sample_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows([listdata])
    writeFile.close()
