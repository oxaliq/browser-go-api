import unittest

from flask import current_app
from flask_testing import TestCase

from ..app import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('browser-go-api.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')