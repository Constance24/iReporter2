from unittest import TestCase
from json import loads, dumps
from app import create_app
import json

app =  create_app()

class RedflagsTestCase(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data={
            "id":1,
            "title":"title"
        }

    def create_incident(self):
        response = self.app.post('/api/v1/redflags', data=json.dumps({
                "createdBy":"xyz", 
                "location":"345,678",
                "image":"wefr",
                "video":"wsqed",
                "comment":"new incidence",
                "incidence_type":"intervention"
                }),content_type = 'application/json')

        return response

    def test_getall_red_flags(self):
        response = self.app.get('/api/v1/redflags')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_can_create_incidence(self):
        response = self.create_incident()
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)

    def test_can_get_all_incidence(self):
        response = self.app.get('/api/v1/redflags')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)


    def test_can_delete_incidence(self):  
        self.create_incident()    
        response = self.app.delete('/api/v1/redflags/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_can_edit_comment_incidence(self):  
        self.create_incident()
        response = self.app.patch('/api/v1/redflags/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 405)


    def test_can_edit_location_incidence(self):  
        self.create_incident()        
        response = self.app.patch('/api/v1/redflags/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 405)

   def test_red_flag_not_found(self):
        response = self.app.get("/api/v1/redflags/17")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200) 
        self.assertIn("Redflag not found",str(result)) 

    def test_wrong_location(self):
        response = self.app.patch("/api/v1/redflags/1/location", headers={'content-Type' : 'application/json'}, data=json.dumps({"locationsss" : "Nairobi"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['data'], "Keyerror: invalid location")

    def test_wrong_comment(self):
        response = self.app.patch("/api/v1/redflags/1/comment", headers={'content-Type' : 'application/json'}, data=json.dumps({"commentsss" : "Nairobi"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['data'], "Keyerror: invalid comment")

