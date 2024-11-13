import os

import faust
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = faust.App(
    "process_member",
    broker=os.environ['BOOTSTRAP_SERVER'],
    value_serializer='json'
)
if __name__ == '__main__':
    app.main()