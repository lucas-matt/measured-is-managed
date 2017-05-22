import unittest
import logging
import os

# set to use unittest database
DB = 'unittest'
os.environ['DBNAME'] = DB

import sys
import persistence.influx as influx
from influxdb import InfluxDBClient
from mim import app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger(__name__)

class TestInflux(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            influx.setup()

    def tearDown(self):
        with app.app_context():
            influx.teardown()

    def test_get_connection(self):
        with app.app_context():
            db = influx.get_db()
            self.assertTrue(isinstance(db, InfluxDBClient))

    def test_connection_cached(self):
        with app.app_context():
            db1 = influx.get_db()
            db2 = influx.get_db()
            self.assertEqual(db1, db2)

    def test_setup(self):
        with app.app_context():
            influx.setup()
            db = InfluxDBClient('influxdb', 8086, 'root', 'root', DB)
            dbs = [entry for entry in db.get_list_database() if entry['name'] == DB]
            self.assertGreater(len(dbs), 0)