
import json
from confluent_kafka import Producer


async def produce():
    conf = {'bootstrap.servers': 'localhost:19092',}
            #'client.id': socket.gethostname()}

    producer = Producer(conf)
    message = {"meu":"vc n sabe oque aconteceu", "os":"caras do charlie brown invadiram a cidade!"}
    producer.produce('NOVO_EXEMPLO_CONFLUENT', value=json.dumps(message).encode('utf-8'))
    producer.flush()
    print('mandou msg')
