import json
import os


from kafka import KafkaProducer



def produce_classes_registration(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_CLASSES_REGISTRATION'],
        value=value,
        key=value['class_id'].encode('utf-8')
    )


