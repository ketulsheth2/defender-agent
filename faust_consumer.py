import faust

topic = 'defender_agent'

app = faust.App('iot_agent', broker='kafka://localhost:9092')

topic = app.topic(topic, value_serializer='json')

@app.agent(topic)
async def consumer(stream):
    """Defender agent consumer"""
    async for value in stream:
        print (value)
        yield value

if __name__ == '__main__':
    app.main() 
