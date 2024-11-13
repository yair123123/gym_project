import json
import os

from kafka import KafkaProducer



def produce_feedback_trainers(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_FEEDBACK_TRAINERS'],
        value=value,
        key=value['member_id'].encode('utf-8')
    )


