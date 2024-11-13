import os

import faust
from dotenv import load_dotenv
from faker.proxy import Faker

from app.processes.main import app

load_dotenv(verbose=True)

member_topic = app.topic(os.environ['TOPIC_MEMBERSHIP_NEW'])
processed_member_topic = app.topic(os.environ['TOPIC_PROCESSED_MEMBERSHIP_NEW'])


@app.agent(member_topic)
async def process_member(messages):
    async for message in messages:
        expiration_date = "-".join(
            map(str, [int(message['join_date'].split("-")[0] )+ 1] + message['join_date'].split("-")[1:]))
        processed_member = ProcessedMember(
            id=message['member_id'],
            name=message['name'],
            email=message['email'],
            join_date=message['join_date'],
            expiration_date=expiration_date,
            membership_type=message['membership_type'],
            recommended_trainer=Faker().name(),
        )
        await processed_member_topic.send(value=processed_member)
        print(f'Send {message}')
class ProcessedMember(faust.Record, serializer='json'):
    id: str
    name: str
    email: str
    join_date: str
    expiration_date: str
    membership_type: str
    recommended_trainer: str
