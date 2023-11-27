# ©<2021> - Wow Labz, Bangalore, India. All rights Reserved.
import logging
from DAO.utils.database_utils import delete_one_record, find_all_records, find_one_record, insert_one_record, update_one_record
from bson.objectid import ObjectId

log = logging.getLogger('dao_log')


async def create_event_service(id, obj, tenant="Schedulebot"):
    try:
        log.debug("Entering create_event_service")
        records_inserted = await insert_one_record('event', obj, tenant)
        if records_inserted:
            log.debug("Exiting create_event_service")
            return str(records_inserted.inserted_id)
        else:
            log.debug("Exiting create_event_service")
            return "Event could not be created"
    except Exception as e:
        log.error(str(e))
        return str(e)


async def edit_event_service(id, updated_keys_obj, tenant="Schedulebot"):
    try:
        log.debug('Entering edit_event_service')
        obj_id = ObjectId(id)
        records_updated = await update_one_record('event', {"_id": obj_id}, {"$set": updated_keys_obj}, tenant)
        if records_updated.modified_count > 0:
            log.debug("Exiting edit_event_service")
            return "Event updated successfully"
        else:
            log.debug("Exiting edit_event_service")
            return "Event not found"
    except Exception as e:
        log.error(str(e))
        return str(e)

async def delete_event_service(id, tenant="Schedulebot"):
    try:
        log.debug('Entering delete_event_service')
        obj_id = ObjectId(id)
        records_deleted = await delete_one_record('event', {"_id": obj_id}, tenant)
        if records_deleted.deleted_count > 0:
            log.debug("Exiting delete_event_service")
            return "Event deleted successfully"
        else:
            log.debug("Exiting delete_event_service")
            return "event not found"
    except Exception as e:
        log.error(str(e))
        return str(e)

def get_one_event_service(query, tenant="Schedulebot"):
    try:
        log.debug("Entering get_one_event_service")
        if query.get('_id'):
            query['_id'] = ObjectId(query['_id'])
        exclude_obj = {'_id':False}
        record_fetched = find_one_record('event', query, tenant, exclude_obj)
        if record_fetched:
            log.debug("Exiting get_one_event_service")
            record_fetched['_id'] = str(query['_id'])
            return record_fetched
        else:
            log.debug("Exiting get_one_event_service")
            return "Event does not exist"
    except Exception as e:
        log.error(str(e))
        return str(e)

def get_all_event_service(query, tenant="Schedulebot", exclude_obj={}):
    try:
        log.debug("Entering get_all_event_service")
        if query.get('_id'):
            query['_id'] = ObjectId(query['_id'])
        
        record_fetched = find_all_records('event', query, tenant)
        if record_fetched:
            records = list(record_fetched)
            for record in records:
                if record.get('_id') and type(record['_id']) == ObjectId:
                    record['_id'] = str(record['_id'])
            log.debug("Exiting get_all_event_service")
            return record_fetched
        else:
            log.debug("Exiting get_all_event_service")
            return "event does not exist"
    except Exception as e:
        log.error(str(e))
        return str(e)
