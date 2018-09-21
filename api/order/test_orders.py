from unittest import TestCase
from views import app

class Testing(TestCase):

    def setUp(self):
        self.client = app.test_client

    def test_get_an_order(self):
        gt = self.client().get('/api/v1/orders')
        self.assertEquals(gt.status_code, 200)