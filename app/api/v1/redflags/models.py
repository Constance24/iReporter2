import datetime

"""This module handles incidence data model"""

db = [] #incidence

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

        db.append(data)

        return {'message':'successfully created',
                'data':data
                }

    def getById():
        pass            


