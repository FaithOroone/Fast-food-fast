from unittest import TestCase
import unittest
import psycopg2
from app.auth.views import app
from app.models.database import DatabaseConnection
from unittest import TestCase
import json
from app.auth.views import app

class Testsignup(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.signup_data ={"user_id":1, "user_name":"faith", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"username":"eunice", "user_password":"faith"}
        self.response = self.client().post('/auth/signup', data=json.dumps({"user_id":2, "user_name":"eunice", "email":"oron@gm.com", "user_password":"faith"}))
        self.db = DatabaseConnection()


    def tearDown(self):
        self.db.drop_table()


    def test_signup(self):
        print ('sss')
        self.assertEqual(self.response.status_code, 201)
        self.assertIn('you have successfully signed up', str(self.response.data))

        response = self.client().post('/auth/signup', data = json.dumps(self.signup_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("username exists", str(response.data))

    def test_login(self):
        response = self.client().post('/auth/login', data=json.dumps(self.login_data),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User logged-in', str(response.data))

