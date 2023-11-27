from database_connector import db

class User:
    def __init__(self):
        self.collection = db["users"]
        pass


    def get_one_user(self, id):
        return self.collection.find_one({"_id":id})
    

    def get_all_users(self, filters):
        return list(self.collection.find())
    
    def create_user(self, data):
        return self.collection.insert_one(data)
    
    def update_user(self, id, new_data):
        return self.collection.update_one({"_id":id}, {"$set":new_data})
    
    def delete_user(self, id):
        return self.collection.delete_one({"_id":id})