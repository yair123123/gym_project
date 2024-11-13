from datetime import datetime
from typing import Dict

from db.repository.regitration_repository import delete_registration


def check_limit_registration(registration:Dict[str,str]):
    if datetime.strptime(registration['end_date'],"%Y-%M-%D") > datetime.now():
        delete_registration(registration)