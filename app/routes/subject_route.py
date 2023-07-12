from flask import Blueprint, jsonify, request
from models.subject import Subject
from bson import json_util
from schema.subject_schema import SubjectSchemaValidator

subject_routes = Blueprint("subjects", __name__)
subject_model = Subject()

@subject_routes.route("/subjects", methods=["GET"])
def get_subjects():
    subjects = subject_model.find_all()
    return json_util.dumps(subjects)

@subject_routes.route("/subjects", methods=["POST"])
def create_subject():
    subject_data = request.get_json()
    validator = SubjectSchemaValidator(subject=subject_data)
    validation_errors = validator.validate()

    if len(validation_errors) > 0:
        response = {
            "status": "error",
            "message": validation_errors
        }
        return jsonify(response), 400
    else:
        result = subject_model.create(subject_data)
        return jsonify({"inserted_id": str(result.inserted_id)})

@subject_routes.route("/subjects/<id>", methods=["GET"])
def get_subject_by_id(id):
    subject = subject_model.find_by_id(id)
    if subject:
        return json_util.dumps(subject)
    else:
        return jsonify({"message": "Subject not found"}), 404
