import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.repository.equipment_audit_repository import insert_equipment

load_dotenv(verbose=True)


def consume_equipment_audit():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EQUIPMENT_AUDIT'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        insert_equipment(message.value)
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_equipment_audit()
    app.run()
