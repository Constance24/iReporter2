from flask_restful import Resource, reqparse
from flask import request, make_response, jsonify
import json

#local import 
from .models import Incidence, db


class RedFlag(Resource):
    def __init__(self):
        self.db = db
        self.id = len(db)+1

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument('createdBy',
                    type=int,
                    required=True,
                    help="Value Must be an Interger as it is an ID or cant be left blank"
                    )

        parser.add_argument('location',
                    type=str,
                    required=True,
                    help="This field cannot be left blank or improperly formated"
                    )
        parser.add_argument('type',
                    type=str,
                    required=True,
                    choices=("red-flag", "intervention"),
                    help="This field cannot be left "
                         "blank or Bad choice: {error_msg}"
                    )
        parser.add_argument('status',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )
        parser.add_argument('images',
                    action='append',
                    help="This field can be left blank!"
                    )
        parser.add_argument('videos',
                    action='append',
                    help="This field can be left blank!"
                    )

        parser.add_argument('comment',
                    type=str,
                    required=True,
                    help="This field cannot be left blank or should be properly formated"
                    )

        data = request.get_json()
        
        new_incidence = Incidence(data['createdBy'],data['image'],data['video'],data['location'], data['comment'], data['incidence_type'])
        output = new_incidence.create_incidence()

        return make_response(jsonify({
            "status" : 201,
            "data" : output,
            "message":"successfully created"
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

    def patch(self, id):
        incident = self.db.find(id)
        if incident:
            incident['comment'] = request.json.get('comment', incident['comment'])
            success_message = {
                        'message' : 'updated comment on redflag record'
            }

            return make_response(jsonify({
                "status" : 201,
                "data" : success_message
            }), 200)

class RedFlagDelete(Resource):
    def __init__(self):
        self.db = db      
    def delete(self, id):
        for incidence in db:
            if incidence['id'] == id:
                db.pop(id - 1)
        return make_response(jsonify({
            "status" : 200,
            "data" : {
            "id" : - 1,
            "message" : "no redflag record" }           
        }), 404)
    

