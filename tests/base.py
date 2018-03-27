import flask
import unittest

from src.server import app as rest_app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.app = flask.Flask('test')
        self.test_client = rest_app.test_client()
