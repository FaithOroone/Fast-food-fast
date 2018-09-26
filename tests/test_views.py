from app.views import app
from unittest import TestCase
import json

class Testing(TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.order_data = {
            "orderId": 1,
            "location": "location",
            "contact": "contact",
            "quantity": "quantity",
            "payment_mode": "payment_mode",
            "status": "stat"
        }

    def test_get_orders(self):
        response = self.app.get(
            '/api/v1/orders', data=json.dumps(self.order_data), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def test_add_an_order(self):
        response = self.app.post(
            '/api/v1/orders', data=json.dumps(self.order_data), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def test_get_an_order(self):
        response = self.app.get('/api/v1/orders/1',
                                data=json.dumps(self.order_data), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def test_update_an_order(self):
        response = self.app.put(
            '/api/v1/orders/2', data=json.dumps(self.order_data), content_type='application/json')
        self.assertEquals(response.status_code, 200)



