import pymongo
from config import CONNECTION_STRING

def create_db_connection():
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["schedulebot"]
    return db