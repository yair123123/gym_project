from typing import Dict

from db.database import classes_collection

def get_by_class_id(class_id:str):
    return classes_collection.find_one({'class_id':class_id})
def insert_registration(registration:Dict[str,str]):
    classes_collection.insert_one(registration)
def delete_registration(registration:Dict[str,str]):
    classes_collection.delete_one(get_by_class_id(registration['class_id']))