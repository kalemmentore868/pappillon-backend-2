from flask import Blueprint, jsonify, request
from models.question_template import Question_Template
from bson import json_util
from schema.question_template_schema import Question_Template_Validator



question_template_routes = Blueprint("question_templates", __name__)
question_template = Question_Template()

@question_template_routes.route("/question_templates", methods=["GET"])
def get_question_templates():
    templates = question_template.find_all()
    return json_util.dumps(templates)

@question_template_routes.route("/question_templates", methods=["POST"])
def create_question_template():
    print("yea")
    question_data = request.get_json()
    _instance = Question_Template_Validator(question_template=question_data)
    response = _instance.validate()

    if len(response) > 0:
        _ = {
            "status": "error",
            "message": response
        }, 403
        return _
    else:
        result = question_template.create(question_data)
        return jsonify({"inserted_id": str(result.inserted_id)})
    

@question_template_routes.route("/question_templates/<id>", methods=["GET"])
def get_question_template(id):
    template = question_template.find_by_id(id)
    if template:
        return json_util.dumps(template)
    else:
        return jsonify({"message": "Template not found"}), 404
    
@question_template_routes.route("/", methods=["GET"])
def test():
    return jsonify({"message": "Hello World"})

