from typing import Dict

from jinja2.lexer import Failure
from pymongo.errors import PyMongoError
from returns.result import Success

from db.database import members_collection, feedback_collection


def insert_feedback(feedback:Dict[str,str]):
    try:
        response = feedback_collection.insert_one(feedback)
        return Success(response)
    except PyMongoError as e:
        return Failure(str(e))