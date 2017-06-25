import sys
import logging
import db_fixture
import services.events as events
from mim import app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class TestEvents(db_fixture.DBTestCase):

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
