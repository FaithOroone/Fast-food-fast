from unittest import TestCase
from app.auth.views import app
from app.models.database import DatabaseConnection
from app.auth.views import app

class BaseTest(TestCase):

    def setUp(self):
        self.client= app.test_client
        self.signup_data ={"user_name":"faith", "email":"oron@gm.com", "user_password":"faith"}
        self.login_data = {"user_name":"faith", "user_password":"faith"}
        self.db = DatabaseConnection()
        self.db.create_tables()


    def tearDown(self):
        self.db.drop_table()