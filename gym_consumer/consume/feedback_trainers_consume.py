import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.repository.feedback_repository import insert_feedback

load_dotenv(verbose=True)


def consume_feedback_trainers():
    consumer = KafkaConsumer(
        os.environ['TOPIC_FEEDBACK_TRAINERS'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        insert_feedback(message.value)
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_feedback_trainers()
