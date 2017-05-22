import persistence.influx as influx
import datetime
import logging

logger = logging.getLogger(__name__)

keys = ['type', 'value']

def __validate_event(evt):
    for key in keys:
        assert key in evt

def save(evt):
    __validate_event(evt)
    db = influx.get_db()
    db.write_points([{
        "measurement": evt['type'],
        "tags": {},
        "time": datetime.datetime.now().isoformat(),
        "fields": {
            "value": evt['value']
        }
    }])