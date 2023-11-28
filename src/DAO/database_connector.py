# import pymongo
from config import CONNECTION_STRING
from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_DETAILS = "mongodb://" + get_config_value('mongo_url') + ':' + str(get_config_value('mongo_port'))
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
client = AsyncIOMotorClient(CONNECTION_STRING)
db = client["Schedulebot1"]
def create_db_connection():
    client = AsyncIOMotorClient(CONNECTION_STRING)
    db = client["Schedulebot"]
    return db
