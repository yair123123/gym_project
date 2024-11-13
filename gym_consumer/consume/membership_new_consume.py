import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.repository.members_repository import insert_member

load_dotenv(verbose=True)


def consume_membership_new():
    consumer = KafkaConsumer(
        os.environ['TOPIC_PROCESSED_MEMBERSHIP_NEW'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:

        print(f'received: {message.key} : {message.value}')
        insert_member(message.value)


app = Flask(__name__)
if __name__ == '__main__':
    consume_membership_new()
