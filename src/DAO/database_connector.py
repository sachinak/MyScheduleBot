import pymongo
from config import CONNECTION_STRING


client = pymongo.MongoClient(CONNECTION_STRING)
db = client["Schedulebot"]
def create_db_connection():
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["Schedulebot"]
    return db
