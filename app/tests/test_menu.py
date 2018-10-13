import json
from unittest import TestCase
from app.auth.views import app
from app.models.database import DatabaseConnection

class Testmenu(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.signup_data ={"user_name":"fai", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"user_name":"fai", "user_password":"faith"}
        self.menu_data = {"menu_id":1, "menu_item":"fish", "price":300}
        self.db = DatabaseConnection()
        self.db.create_tables()


    def tearDown(self):
        self.db.drop_table()

    def test_menu(self):
        response = self.client().post('/auth/signup', json=self.signup_data)
        login_response = self.client().post('/auth/login', json=self.login_data)
        response = self.client().post('/menu', headers=({"x-access-token":login_response.json['token']}))
        #self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'Menu item added successfully')

