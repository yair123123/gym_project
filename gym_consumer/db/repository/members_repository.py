from typing import Dict

from jinja2.lexer import Failure
from pymongo.errors import PyMongoError
from returns.result import Success

from db.database import members_collection


def insert_member(member:Dict[str,str]):
    try:
        response = members_collection.insert_one(member)
        return Success(response)
    except PyMongoError as e:
        return Failure(str(e))