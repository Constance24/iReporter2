from flask_restful import Resource
from flask import request, make_response, jsonify
import json
 
from .models import db


class RedFlag(Resource):
    def __init__(self):
        self.db = db
        self.id = len(db)+1

    def get(self):
        return db, 200
        
    def post(self):
        success_message = {
            'message' : 'Success created a redflag'
        }
        return make_response(jsonify({
            "status" : 201,
            "message" : success_message
        }), 201)


    
