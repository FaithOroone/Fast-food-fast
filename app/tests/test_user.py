from unittest import TestCase
import unittest
import psycopg2
from app.auth.views import app
from app.models.database import DatabaseConnection
import jwt
import json

class Testsignup(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.signup_data ={"user_id":1, "user_name":"faith", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"username":"faith", "user_password":"faith"}

    # def test_signup(self):
    #     response = self.client().post('/auth/signup', data=json.dumps(self.signup_data),
    #     content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('you have successfully loged in', json.loads(response.data)['message'])


    #existing user
    def testuserexists(self):
        response = self.client().post('/auth/signup', data = json.dumps(self.signup_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("username exists", str(response.data))

    # def testlogin(self):
    #     response = self.client().post('/auth/login', data = json.dumps(self.login_data), content_type = 'application/json')
    #     self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main