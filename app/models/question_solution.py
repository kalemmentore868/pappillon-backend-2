from config import mongo
from bson.objectid import ObjectId

class Question_Solution:
    def create(self, question_solution):
        return mongo.db.question_solutions.insert_one(question_solution)
    
    def find_all(self):
        return list(mongo.db.question_solutions.find())

    def find_by_id(self, id):
        obj_id = ObjectId(id)
        return mongo.db.question_solutions.find_one({"_id": obj_id})
