import sys
import logging
import os
import unittest

# set to use unittest database
DB = 'unittest'
os.environ['DBNAME'] = DB

import persistence.influx as influx
from mim import app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class DBTestCase(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            influx.setup()

    def tearDown(self):
        with app.app_context():
            influx.teardown()

    def get_db_name(self):
        return DB
