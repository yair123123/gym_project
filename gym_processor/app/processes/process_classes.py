import os

import faust
from dotenv import load_dotenv

from app.processes.main import app

registration_topic = app.topic(os.environ['TOPIC_CLASSES_REGISTRATION'])
limit_topic = app.topic(os.environ['TOPIC_PROCESSED_CLASSES_LIMIT'])

load_dotenv(verbose=True)


@app.agent(registration_topic)
async def process_limit(messages):
    async for message in messages:
        end_date = "-".join(
            map(str, [int(message['join_date'].split("-")[0]) + 1] + message['join_date'].split("-")[1:]))

        new_registration = ProcessedLimit(
            class_id=message['class_id'],
            member_id=message['member_id'],
            registration_date=message['registration_date'],
            end_date=end_date
        )
        await limit_topic.send(value=new_registration)
        print(f'Send {message}')


class ProcessedLimit(faust.Record, serializer='json'):
    class_id: str
    member_id: str
    registration_date: str
    end_date: str
