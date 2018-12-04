from flask_restful import Resource
from flask import request, make_response, jsonify


#local import 
from .models import Incidence, db


class RedFlag(Resource):
    def __init__(self):
        self.db = db
        self.id = len(db)+1


    def get(self):
        return db,200

    def post(self):
        data = request.get_json()
        
        new_incidence = Incidence(data['createdBy'],data['image'],data['video'],data['location'], data['comment'], data['incidence_type'])
        output = new_incidence.create_incidence()

        return make_response(jsonify({
            "status" : 201,
            "data" : "successfully created"
            }), 201)



    

class RedFlagDelete(Resource):
    def delete(self, id):
        for incidence in db:
            if incidence['id'] == id:
                db.pop(id - 1)
                success_message = {
                'id' : id,
                'message' : 'Red-Flag Deleted successfully'
                }
        return make_response(jsonify({
            "status" : 204,
            "data" : success_message
            }), 204)

    
class ManageRedFlag(Resource):
    def __init__(self):
        self.db = db

    def get(self, id):
        incident = self.getById(id)

        for item in db:
            if item['id'] == id:
                return item, 200

        return item,200


    def getById(self, id):
       
        pass

    def patch(self, id):
        incident = self.db.find(id)
        if incident:
            incident['location'] = request.json.get('location', incident['location'])
            success_message = {
                        'message' : 'updated location of redflag record'
            }

            return make_response(jsonify({
                "status" : 201,
                "data" : success_message
            }), 201)


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
            }), 201)


    


    