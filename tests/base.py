from flask_testing import TestCase
from ..app import app, db

class BaseTestCase(TestCase):
    """ Base Tests """
    
    def create_app(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass