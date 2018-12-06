from flask_restful import Resource
from flask import request, make_response, jsonify


#local import 
from .models import Incidence, db


class RedFlag(Resource):
    def __init__(self):
        self.db = db
        self.id = len(db)+1

    def post(self):
        data = request.get_json()
        
        new_incidence = Incidence(data['createdBy'],data['image'],data['video'],data['location'], data['comment'], data['incidence_type'])
        output = new_incidence.create_incidence()

        return make_response(jsonify({
            "status" : 201,
            "data" : "successfully created"
            }), 201)

    def get(self):
        return db,200

class ManageRedFlag(Resource):
    def __init__(self):
        self.db = db

    def getById(self, id):
       for item in db:
            if item['id'] == id:
                return item, 200

def patch(self, id):
        incident = self.db.find(id)
        if incident:
            incident['location'] = request.json.get('location', incident['location'])
            success_message = {
                        'message' : 'updated location of redflag record'
            }

            return make_response(jsonify({
                "status" : 200,
                "data" : success_message
            }), 200)


    

