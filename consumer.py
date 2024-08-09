
from confluent_kafka import Consumer
from func import dummy_func


async def consume():
    consumer_conf = {
        'bootstrap.servers': 'localhost:19092',
        'group.id': 'consumer-local-teste-nojento',
        'enable.auto.commit': True,
        'auto.offset.reset': 'earliest',
    }
    consumer = Consumer(consumer_conf)

    topic = ['NOVO_EXEMPLO_CONFLUENT']
    #topic = 'API_IMAGE_MANAGER_PLANTS,API_IMAGE_MANAGER_LEAF_DAMAGE,API_IMAGE_MANAGER_PLAGUES'.split(',')
    consumer.subscribe(topic)

    #essa porcaria toda abaixo serve no caso de 'enable.auto.commit': True
    #partitions = consumer.assignment()
    #consumer.assign(partitions)
    #committed_offsets = consumer.committed(partitions)
    #for tp, offset in zip(partitions, committed_offsets):
    #    if offset.offset == -1001:
    #        print(f"Partição {tp.partition} ainda não tem um offset commitado.")
    #    else:
    #        print(f"Último offset commitado para a partição {tp.partition}: {offset.offset}")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            try:
                if not await dummy_func(msg.value()):

                    raise Exception (f'\nPROCESSING FAILED')
                #else:
                #    consumer.commit(asynchronous=False)
            except Exception as e:
                print('manda para DLQ aqui')
                #consumer.commit(asynchronous=False)
                continue
    finally:
        consumer.close()
