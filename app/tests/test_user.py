import json
from .base import BaseTest

class Testsignup(BaseTest):


    def test_signup(self):
        response = self.client().post('/auth/signup', json=self.signup_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'you have successfully signed up')

    def test_login(self):
        self.client().post('/auth/signup', json=self.signup_data)
        response = self.client().post('/auth/login', json=self.login_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'User logged-in')

