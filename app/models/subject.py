from config import mongo
from bson.objectid import ObjectId

class Subject:
    def create(self, subject):
        return mongo.db.subjects.insert_one(subject)
    
    def find_all(self):
        return list(mongo.db.subjects.find())

    def find_by_id(self, id):
        obj_id = ObjectId(id)
        return mongo.db.subjects.find_one({"_id": obj_id})
