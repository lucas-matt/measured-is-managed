import sys
import logging
import os

# set to use unittest database
DB = 'unittest'
os.environ['DBNAME'] = DB

import unittest
import services.events as events
import persistence.influx as influx
from mim import app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


class TestEvents(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            influx.setup()

    def tearDown(self):
        with app.app_context():
            influx.teardown()

    def test_missing_type(self):
        with app.app_context():
            with self.assertRaises(AssertionError):
                events.save({'value': 8.0})

    def test_missing_value(self):
        with app.app_context():
            with self.assertRaises(AssertionError):
                events.save({'type': 'exercise'})

    def test_save(self):
        with app.app_context():
            events.save({'type': 'exercise', 'value': 8.0})