
from confluent_kafka.admin import AdminClient, NewTopic

async def create():
    print('vai criar o tópico em....')
    admin_client = AdminClient({
        "bootstrap.servers": 'localhost:19092'
    })

    topic_list = []
    #se liga nessas configs
    #https://kafka.apache.org/documentation.html#topicconfigs
    topic_list.append(NewTopic("NOVO_EXEMPLO_CONFLUENT", 3, 3))
    admin_client.create_topics(topic_list)
    print('tópico criado em!')
