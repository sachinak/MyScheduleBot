import pymongo
from config import connection_string, db_name


def create_db_connection():
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    return db
