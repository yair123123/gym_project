import os

from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv(verbose=True)
client = MongoClient(os.environ['DB_URL'])

db = client['gym']

members_collection = db['members']
classes_collection = db['classes']
feedback_collection = db['feedback']
equipment_collection = db['equipment']