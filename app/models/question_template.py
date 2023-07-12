from config import mongo
from bson.objectid import ObjectId

class Question_Template:
    def create(self, question_template):
        return mongo.db.question_templates.insert_one(question_template)
    
    def find_all(self):
        return list(mongo.db.question_templates.find())

    def find_by_id(self, id):
        obj_id = ObjectId(id)
        return mongo.db.question_templates.find_one({"_id": obj_id})
