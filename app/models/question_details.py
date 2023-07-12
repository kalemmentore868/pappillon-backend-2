from config import mongo
from bson.objectid import ObjectId

class Question_Details:
    def create(self, question_details):
        return mongo.db.question_details.insert_one(question_details)
    
    def find_all(self):
        return list(mongo.db.question_details.find())

    def find_by_id(self, id):
        obj_id = ObjectId(id)
        return mongo.db.question_details.find_one({"_id": obj_id})
