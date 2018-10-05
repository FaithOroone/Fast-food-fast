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
        self.order_data ={"user_id":1, "menu_id":1, "contact":7545544544,"quantity":5, "order_status":"new"}
        self.db = DatabaseConnection()

    def tearDown(self):
        self.db.drop_table()


    def test_make_order(self):
        response = self.client().post('/users/orders', data=json.dumps(self.order_data),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created', str(response.data))

