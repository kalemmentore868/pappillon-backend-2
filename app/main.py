from flask import Flask
from flask import request, jsonify
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



def get_client_ip():
    # Check for the X-Forwarded-For header to get the client's public IP address
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # The X-Forwarded-For header can contain a comma-separated list of IPs.
        # The client's IP address will be the first one in the list.
        return x_forwarded_for.split(',')[0]
    else:
        # If X-Forwarded-For is not available, use request.remote_addr as a fallback
        return request.remote_addr

@app.route('/api/getIP', methods=['GET'])
def get_ip():
    client_ip = get_client_ip()
    return jsonify(ip=client_ip)

if __name__ == "__main__":
    app.run(debug=True)


