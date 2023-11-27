# ©<2021> - Wow Labz, Bangalore, India. All rights Reserved.
import motor.motor_asyncio
import logging
from core_config.core_config import get_config_value
log = logging.getLogger("dao_log")
from DAO.database_connector import create_db_connection
# MONGO_DETAILS = "mongodb://" + get_config_value('mongo_url') + ':' + str(get_config_value('mongo_port'))
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

try:
    db = create_db_connection()
except Exception as ex:
    log.error("Exception occured " + str(ex))
    raise ex



async def find_one_record(collection, query, tenant="Schedulebot", exclude_obj={}):
    try:
        log.debug("Entering find_one_record")
        database = db
        #database = client['testDB']
        collection_obj = database.get_collection(collection)
        if exclude_obj:
            obj_found = await collection_obj.find_one(query, exclude_obj)
        else:
            obj_found = await collection_obj.find_one(query)
        if obj_found:
            if obj_found.get('_id'):
                obj_found['_id'] = str(obj_found['_id'])
        log.debug("Exiting find_one_record")
        return obj_found
    except Exception as ex:
        log.error("Exception occurred in find_one_record: " + str(ex))
        raise ex


async def insert_one_record(collection, data, tenant="Schedulebot"):
    try:
        log.debug("Entering insert_one_record")
        database = db
        collection_obj = database.get_collection(collection)
        log.debug("Exiting insert_one_record")
        obj_inserted = await collection_obj.insert_one(data)
        return obj_inserted
    except Exception as ex:
        log.error("Exception occurred in insert_one_record: " + str(ex))
        raise ex


async def find_all_records(collection, query, tenant="Schedulebot", exclude_obj={}):
    try:
        log.debug("Entering find_all_records")
        data_list = []
        database = db
        collection_obj = database.get_collection(collection)
        if exclude_obj:
            async for obj_data in collection_obj.find(query, exclude_obj):
                data_list.append(obj_data)
        else:
            async for obj_data in collection_obj.find(query):
                data_list.append(obj_data)
        log.debug("Exiting find_all_records")
        return data_list
    except Exception as ex:
        log.error("Exception occurred in find_all_records: " + str(ex))
        raise ex


async def update_one_record(collection, query, data, tenant="Schedulebot"):
    try:
        log.debug("Entering update_one_record")
        database = db
        collection_obj = database.get_collection(collection)
        record_found = await find_one_record(collection, query, tenant)
        record_updated = False
        if record_found:
            record_updated = await collection_obj.update_one(query, data)
        log.debug("Exiting update_one_record")
        return record_updated
    except Exception as ex:
        log.error("Exception occurred in update_one_record: " + str(ex))
        raise ex


async def update_all_records(collection, query, data, tenant="Schedulebot"):
    try:
        log.debug("Entering update_all_records")
        database = db
        collection_obj = database.get_collection(collection)
        record_found = await find_one_record(collection, query, tenant)
        records_updated = False
        if record_found:
            records_updated = collection_obj.update(query, {data})
        log.debug("Exiting update_all_records")
        return records_updated
    except Exception as ex:
        log.error("Exception occurred in update_all_records: " + str(ex))
        raise ex


async def delete_one_record(collection, query, tenant="Schedulebot"):
    try:
        log.debug("Entering delete_one_record")
        database = db
        collection_obj = database.get_collection(collection)
        record_deleted = False
        record_found = await find_one_record(collection, query, tenant)
        if record_found:
            record_deleted = collection_obj.delete_one(query)
        log.debug("Exiting delete_one_record")
        return record_deleted
    except Exception as ex:
        log.error("Exception occurred in delete_one_record: " + str(ex))
        raise ex

async def delete_many_record(collection, query, tenant="Schedulebot"):
    try:
        log.debug("Entering delete_many_record")
        database = db
        collection_obj = database.get_collection(collection)
        record_deleted = False
        record_found = await find_one_record(collection, query, tenant)
        if record_found:
            record_deleted = await collection_obj.delete_many(query)
        log.debug("Exiting delete_many_record")
        return record_deleted
    except Exception as ex:
        log.error("Exception occurred in delete_many_record: " + str(ex))
        raise ex
