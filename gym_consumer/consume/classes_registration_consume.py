import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.repository.regitration_repository import insert_registration

load_dotenv(verbose=True)


def consume_classes_registration():
    consumer = KafkaConsumer(
        os.environ['TOPIC_CLASSES_REGISTRATION'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('lisining...')
    for message in consumer:
        insert_registration(message.value)
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_classes_registration()
