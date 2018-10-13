from unittest import TestCase
from app.auth.views import app
from app.models.database import DatabaseConnection
import json

class Testorders(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.order_data={"user_id":1, "menu_id":2, "contact":123456789, "quantity":6, "order_status":"new"}
        self.db = DatabaseConnection()
        self.db.create_tables()


    def tearDown(self):
        self.db.drop_tableorders()


    def test_add_an_order(self):
        response = self.client().post('/users/orders', json=self.order_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'Order created')