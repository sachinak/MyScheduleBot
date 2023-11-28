import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def find_documents():
    try:
        # Connect to MongoDB asynchronously
        client = AsyncIOMotorClient("mongodb://localhost:27017/")
        db = client["Schedulebot"]
        collection = db["event"]

        # Try to find documents in the collection
        cursor = collection.find()
        print("HEHE")

        # Iterate over the cursor asynchronously
        async for document in cursor:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")
async def find_one_record(collection, query, tenant="Schedulebot", exclude_obj={}):
    try:
        # log.debug("Entering find_one_record")
        client = AsyncIOMotorClient("mongodb://localhost:27017/")
        database = client["Schedulebot"]
        #database = client['testDB']
        collection_obj = database.get_collection(collection)
        if exclude_obj:
            obj_found = await collection_obj.find_one(query, exclude_obj)
        else:
            obj_found = await collection_obj.find_one(query)
        if obj_found:
            if obj_found.get('_id'):
                obj_found['_id'] = str(obj_found['_id'])
        # log.debug("Exiting find_one_record")
        data_obj = {"user_id":"Sachin"}
        await collection_obj.insert_one(data_obj)

        print(obj_found)
        return obj_found
    except Exception as ex:
        # log.error("Exception occurred in find_one_record: " + str(ex))
        raise ex
# Create an event loop
loop = asyncio.get_event_loop()

# Run the event loop
loop.run_until_complete(find_one_record("event", {"user_id":"Sachin"}))

# Close the loop
loop.close()
