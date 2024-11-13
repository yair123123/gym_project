import json
import os

from kafka import KafkaProducer



def produce_equipment_audit(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_EQUIPMENT_AUDIT'],
        value=value,
        key=value['equipment_id'].encode('utf-8')
    )

