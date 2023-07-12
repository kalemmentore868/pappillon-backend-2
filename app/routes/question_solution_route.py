from flask import Blueprint, jsonify, request
from models.question_solution import Question_Solution
from bson import json_util
from schema.question_solution_schema import Question_Solution_Validator

question_solution_routes = Blueprint("question_solutions", __name__)
question_solution = Question_Solution()

@question_solution_routes.route("/question_solutions", methods=["GET"])
def get_question_solutions():
    solutions = question_solution.find_all()
    return json_util.dumps(solutions)

@question_solution_routes.route("/question_solutions", methods=["POST"])
def create_question_solution():
    solution_data = request.get_json()
    _instance = Question_Solution_Validator(question_solution=solution_data)
    response = _instance.validate()

    if len(response) > 0:
        _ = {
            "status": "error",
            "message": response
        }, 403
        return _
    else:
        result = question_solution.create(solution_data)
        return jsonify({"inserted_id": str(result.inserted_id)})

@question_solution_routes.route("/question_solutions/<id>", methods=["GET"])
def get_question_solution_by_id(id):
    solution = question_solution.find_by_id(id)
    if solution:
        return json_util.dumps(solution)
    else:
        return jsonify({"message": "Solution not found"}), 404
