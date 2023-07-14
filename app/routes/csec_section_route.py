from flask import Blueprint, jsonify, request
from models.csec_section import CSEC_Section
from bson import json_util
from schema.csec_section_schema import CSEC_SectionSchemaValidator

csec_section_routes = Blueprint("csec_sections", __name__)
csec_section_model = CSEC_Section()

@csec_section_routes.route("/csec_sections", methods=["GET"])
def get_csec_sections():
    csec_sections = csec_section_model.find_all()
    return json_util.dumps(csec_sections)

@csec_section_routes.route("/csec_sections", methods=["POST"])
def create_csec_section():
    csec_section_data = request.get_json()
    validator = CSEC_SectionSchemaValidator(csec_section=csec_section_data)
    validation_errors = validator.validate()

    if len(validation_errors) > 0:
        response = {
            "status": "error",
            "message": validation_errors
        }
        return jsonify(response), 400
    else:
        result = csec_section_model.create(csec_section_data)
        return jsonify({"inserted_id": str(result.inserted_id)})
    

@csec_section_routes.route("/csec_sections/<id>", methods=["GET"])
def get_csec_section_by_id(id):
    csec_section = csec_section_model.find_by_id(id)
    if csec_section:
        return json_util.dumps(csec_section)
    else:
        return jsonify({"message": "CSEC section not found"}), 404

@csec_section_routes.route("/csec_sections/by_subject/<subject_id>", methods=["GET"])
def get_csec_sections_by_subject(subject_id):
    csec_sections = csec_section_model.find_by_subject_id(subject_id)
    return json_util.dumps(csec_sections)