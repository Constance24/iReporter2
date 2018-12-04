from flask_restful import Resource
from flask import request, make_response, jsonify
import json


#local import 
from .models import Incidence, db


class RedFlag(Resource):
    def __init__(self):
        self.db = db
        self.id = len(db)+1
        
    def post(self):
        data = request.get_json()
        new_incidence = Incidence(data['createdBy'],data['image'],data['video'],
        data['location'], data['comment'], data['incidence_type'])
        output = new_incidence.create_incidence()

        return make_response(jsonify({
            "status" : 201,
            "data" : "successfully created"
            }), 201)

