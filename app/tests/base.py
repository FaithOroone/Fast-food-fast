from unittest import TestCase
from app.auth.views import app
from app.models.database import DatabaseConnection

class BaseTest(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.signup_data ={"user_name":"faith", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"user_name":"faith", "user_password":"faith"}
        #self.order_data={"user_id":1, "menu_id":2, "contact":1234567, "quantity":6, "order_status":"new"}
        self.db = DatabaseConnection()
        self.db.create_tables()


    def tearDown(self):
        self.db.drop_table()