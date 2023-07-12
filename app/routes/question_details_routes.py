from flask import Blueprint, jsonify, request
from models.question_details import Question_Details
from bson import json_util
from schema.question_details_schema import Question_Details_Validator

question_details_routes = Blueprint("question_details", __name__)
question_details = Question_Details()

@question_details_routes.route("/question_details", methods=["GET"])
def get_question_details():
    details = question_details.find_all()
    return json_util.dumps(details)

@question_details_routes.route("/question_details", methods=["POST"])
def create_question_details():
    details_data = request.get_json()
    print(details_data)
    _instance = Question_Details_Validator(question_details=details_data)
    response = _instance.validate()

    if len(response) > 0:
        _ = {
            "status": "error",
            "message": response
        }, 403
        return _
    else:
        result = question_details.create(details_data)
        return jsonify({"inserted_id": str(result.inserted_id)})


@question_details_routes.route("/question_details/<id>", methods=["GET"])
def get_question_details_by_id(id):
    details = question_details.find_by_id(id)
    if details:
        return json_util.dumps(details)
    else:
        return jsonify({"message": "Details not found"}), 404
