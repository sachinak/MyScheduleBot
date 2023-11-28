# ©<2021> - Wow Labz, Bangalore, India. All rights Reserved.
import logging
from src.DAO.utils.database_utils import delete_one_record, find_all_records, find_one_record, insert_one_record, update_one_record
from bson.objectid import ObjectId

log = logging.getLogger('dao_log')


async def create_schedule_service(id, obj, tenant):
    try:
        log.debug("Entering create_schedule_service")
        records_inserted = await insert_one_record('schedule', obj, tenant)
        if records_inserted:
            log.debug("Exiting create_schedule_service")
            return str(records_inserted.inserted_id)
        else:
            log.debug("Exiting create_schedule_service")
            return "Schedule could not be created"
    except Exception as e:
        log.error(str(e))
        return str(e)


async def edit_schedule_service(id, updated_keys_obj, tenant):
    try:
        log.debug('Entering edit_schedule_service')
        obj_id = ObjectId(id)
        records_updated = await update_one_record('schedule', {"_id": obj_id}, {"$set": updated_keys_obj}, tenant)
        if records_updated.modified_count > 0:
            log.debug("Exiting edit_schedule_service")
            return "schedule updated successfully"
        else:
            log.debug("Exiting edit_schedule_service")
            return "schedule not found"
    except Exception as e:
        log.error(str(e))
        return str(e)

async def delete_schedule_service(id, tenant):
    try:
        log.debug('Entering delete_schedule_service')
        obj_id = ObjectId(id)
        records_deleted = await delete_one_record('schedule', {"_id": obj_id}, tenant)
        if records_deleted.deleted_count > 0:
            log.debug("Exiting delete_schedule_service")
            return "Form deleted successfully"
        else:
            log.debug("Exiting delete_schedule_service")
            return "schedule not found"
    except Exception as e:
        log.error(str(e))
        return str(e)

async def get_one_schedule_service(query, tenant):
    try:
        log.debug("Entering get_one_schedule_service")
        if query.get('_id'):
            query['_id'] = ObjectId(query['_id'])
        exclude_obj = {'_id':False}
        record_fetched = await find_one_record('schedule', query, tenant, exclude_obj)
        if record_fetched:
            log.debug("Exiting get_one_schedule_service")
            record_fetched['_id'] = str(query['_id'])
            return record_fetched
        else:
            log.debug("Exiting get_one_schedule_service")
            return "schedule does not exist"
    except Exception as e:
        log.error(str(e))
        return str(e)

async def get_all_schedules_service(query, tenant, exclude_obj={}):
    try:
        log.debug("Entering get_all_schedules_service")
        if query.get('_id'):
            query['_id'] = ObjectId(query['_id'])
        
        record_fetched = await find_all_records('schedule', query, tenant)
        if record_fetched:
            records = list(record_fetched)
            for record in records:
                if record.get('_id') and type(record['_id']) == ObjectId:
                    record['_id'] = str(record['_id'])
            log.debug("Exiting get_all_schedules_service")
            return record_fetched
        else:
            log.debug("Exiting get_all_schedules_service")
            return "schedule does not exist"
    except Exception as e:
        log.error(str(e))
        return str(e)
