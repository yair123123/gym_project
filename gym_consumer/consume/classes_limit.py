import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.repository.regitration_repository import insert_registration
from service.classes_service import check_limit_registration

load_dotenv(verbose=True)


def consume_classes_registration():
    consumer = KafkaConsumer(
        os.environ['TOPIC_PROCESSED_CLASSES_LIMIT'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('listening...')
    for message in consumer:
        check_limit_registration(message.value)
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_classes_registration()
