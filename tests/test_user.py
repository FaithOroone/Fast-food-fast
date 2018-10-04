from unittest import TestCase
import unittest
from app.auth.views import app
from app.models.database import DatabaseConnection
import jwt
import json

class Testing(TestCase):

    def setUp(self):
        self.client = app.test_client
        self.signup_data ={"user_id":1, "user_name":"faith", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"username":"faith", "user_password":"faith"}

    def test_signup(self):
        response = self.client().post('/auth/signup', data = json.dumps(self.signup_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("you have successfully loged in", str(response.data))

if __name__ == '__main__':
    unittest.main