import json
import os
from typing import Dict

from kafka import KafkaProducer



def produce_membership_details(membership_details:Dict[str,str]):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_MEMBERSHIP_NEW'],
        value=membership_details,
        key=membership_details['member_id'].encode('utf-8')
    )


