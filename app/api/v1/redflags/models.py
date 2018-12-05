import datetime
from flask import request
from flask_restful import reqparse

"""This module handles incidence data model"""

db = [] #incidence
parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('createdBy',
                    type=str,
                    required=True,
                    help="Please fill this field"
                    )

parser.add_argument('location',
                    type=str,
                    required=True,
                    help="Please fill this field"
                    )

parser.add_argument('images',
                    action='append',
                    help="Please fill this field"
                    )

parser.add_argument('videos',
                    action='append',
                    help="Please fill this field"
                    )

parser.add_argument('comment',
                    type=str,
                    required=True,
                    help="Please fill in this field"
                    )

class Incidence:
    def __init__(self, createdBy, location,image, video, comment, incidence_type): 
        """creates instance variables for the Incidence class"""
        self.counter = 0
        self.status = 'draft'
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.image = image
        self.video = video
        self.createdBy = createdBy
        self.location = location
        self.comment = comment
        self.incidence_type = incidence_type

    def get_all_incidences(self):
        return db
    
    def create_incidence(self):
        args = parser.parse_args()
        data = {}
        data['id'] = len(db)+1
        data['status'] = self.status
        data['createdOn'] = self.createdOn
        data['image'] = self.image
        data['video'] = self.video
        data['createdBy'] = self.createdBy
        data['location'] = self.location
        data['comment'] = self.comment
        data['incidence_type'] = self.incidence_type

        if data["id"] == "keyerror":
            return "keyerror"
        
        self.db.append(data)
        return self.id

        return {'message':'successfully created',
                'data':data
                }

    def getById():
        pass            


    def edit_redflag_location(self,incident):
        incident['location'] = request.json.get('location','keyerror')
        if incident['location'] == 'keyerror':
            return "keyerror"
        return "updated location"


    def edit_redflag_comment(self,incident):
        incident['comment'] = request.json.get('comment','keyerror')
        if incident['comment'] == 'keyerror':
            return "keyerror"
        return "updated comment"


    def delete(self, incident):
        self.db.remove(incident)
        return "deleted" 