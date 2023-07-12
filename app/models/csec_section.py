from config import mongo
from bson.objectid import ObjectId

class CSEC_Section:
    def create(self, csec_section):
        return mongo.db.csec_sections.insert_one(csec_section)
    
    def find_all(self):
        return list(mongo.db.csec_sections.find())

    def find_by_id(self, id):
        obj_id = ObjectId(id)
        return mongo.db.csec_sections.find_one({"_id": obj_id})
