import datetime
from flask_restful import Resource
"""This module handles incidence data model"""
db = []
class Incidence:
    count = 0
    def __init__(self, createdBy, location,image, video, comment, incidence_type): 
        """creates instance variables for the Incidence class"""
        self.status = 'draft'
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.image = image
        self.video = video
        self.createdBy = createdBy
        self.location = location
        self.comment = comment
        self.incidence_type = incidence_type
        self.id = count + 1
        count +=1 

    def get_all_incidences(self):
        return db
    
    def create_incidence(self):
        db.append(self.__dict__)
        return data
        
    def getById():
        pass            

    def edit_redflag_location(self, incident):
        """Method to edit a redflag's location"""
        incident['location'] = request.json.get('location', 'keyerror')
        if incident['location'] == 'keyerror':
            return "keyerror"
        return "updated"

    def edit_redflag_comment(self, incident):
        """Method to edit a redflag's comment"""
        incident['comment'] = request.json.get('comment', 'keyerror')
        if incident['comment'] == 'keyerror':
            return "keyerror"
        return "updated"