import json
from .base import BaseTest

class Testorders(BaseTest):


    def test_add_an_order(self):
        response = self.client().post('/users/orders', json=self.order_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'Order created')