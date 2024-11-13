from typing import Dict

from jinja2.lexer import Failure
from pymongo.errors import PyMongoError
from returns.result import Success

from db.database import members_collection, equipment_collection


def insert_equipment(equipment:Dict[str,str]):
    try:
        response = equipment_collection.insert_one(equipment)
        return Success(response)
    except PyMongoError as e:
        return Failure(str(e))