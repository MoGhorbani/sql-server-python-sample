from flask import Flask, jsonify,request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json
from db import insert_person,get_person
app = Flask(__name__)
api = Api(app)

# Define a sample resource
class HelloWorld(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

# Add the resource to the API
api.add_resource(HelloWorld, '/hello')


# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

@app.route('/person/insert', methods=['POST'])
def insert():
    data = request.get_json()
    fname = data.get('fname')
    lname = data.get('lname')
    insert_person(fname,lname)
    return "Student inserted successfully!"

@app.route('/person/get', methods=['GET'])
def get():
    person_id = request.args.get('id')
    person = get_person(person_id)
    return json.dumps(person, default=str)

if __name__ == '__main__':
    app.run(debug=True)