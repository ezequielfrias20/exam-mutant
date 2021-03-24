"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Mutation,NoMutation
from mutant import Mutant
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/mutation', methods=['POST'])
def check_mutant():
    body= request.get_json()
    #validaciones de body para campos obligatorios 
    if isinstance (body,dict):
        if body is None:
            raise APIException("Please specify the request body as a json object", status_code=400)
        if 'dna' not in body:
            raise APIException("You need to specify dna", status_code=400)

    else: 
        return "error in body, is not a dictionary"
    if Mutant(body['dna']):
        Mutation.create()
        return "Es mutante",200
    elif Mutant(body['dna'])==False:
        NoMutation.create()
        return "No es Mutante",403
    else:
        raise APIException("La matriz tiene que ser NxN y los unicos valores permitidos son A T C G", status_code=400)

@app.route('/stats', methods=['GET'])
def count():
    mutation = Mutation.query.all()
    no_mutation= NoMutation.query.all()
    response_body= {"count_mutations":len(mutation),
    "count_no_mutation":len(no_mutation),
    "ratio":len(mutation)/len(no_mutation)}
    return jsonify(response_body),200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
