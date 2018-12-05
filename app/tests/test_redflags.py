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

    def test_getall_redflags(self):
        response = self.app.get('/api/v1/redflags')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_can_create_incidence(self):
       
        response = self.create_incident()
        # self.assertEqual(response.json.get('message'), expected)
        self.assertEqual(response.status_code, 201)

    def test_can_get_all_incidence(self):
        response = self.app.get('/api/v1/redflags')

        expected = '200'

        self.assertEqual(response.status_code, 200)


    def test_can_delete_incidence(self):  
        self.create_incident()
        
        response = self.app.delete('/api/v1/redflags/1')

        self.assertEqual(response.status_code, 204)

    def test_can_edit_comment_incidence(self):  
        self.create_incident()
            
        response = self.app.patch('/api/v1/redflags/1')

        self.assertEqual(response.status_code, 405)


    def test_can_edit_location_incidence(self):  
        self.create_incident()
            
        response = self.app.patch('/api/v1/redflags/1')

        self.assertEqual(response.status_code, 405)


   

