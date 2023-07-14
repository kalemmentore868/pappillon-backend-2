from flask import Flask
from config import app, mongo
from routes.question_template_routes import question_template_routes
from routes.question_details_routes import question_details_routes
from routes.question_solution_route import question_solution_routes
from routes.subject_route import subject_routes
from routes.csec_section_route import csec_section_routes


api_prefix = '/api'  # Define the API prefix here

app.register_blueprint(question_template_routes, url_prefix=api_prefix)
app.register_blueprint(question_details_routes, url_prefix=api_prefix)
app.register_blueprint(question_solution_routes, url_prefix=api_prefix)
app.register_blueprint(subject_routes, url_prefix=api_prefix)
app.register_blueprint(csec_section_routes, url_prefix=api_prefix)

if __name__ == "__main__":
    app.run(debug=True)
