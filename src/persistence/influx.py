import os
import logging
from flask import g
from influxdb import InfluxDBClient

logger = logging.getLogger(__name__)

def __read_env():
    """
    Read environment variables for database details
    """
    environ = os.environ
    host = environ.get('DBHOST', 'influxdb')
    port = int(environ.get('DBPORT', '8086'))
    user = environ.get('DBUSER', 'root')
    password = environ.get('DBPASS', 'root')
    db = environ.get('DBNAME', 'mim')
    return (host, port, user, password, db)

def __create_client(creds_tuple=__read_env()):
    return InfluxDBClient(*creds_tuple)

def get_db():
    if not hasattr(g, 'influx_db'):
        g.influx_db = __create_client()
    return g.influx_db

def db_name():
    return __read_env()[4]

def setup():
    db = get_db()
    name = db_name()
    logger.info("Setting up %s", name)
    db.create_database(name)

def teardown():
    db = get_db()
    name = db_name()
    logger.info("Tearing down %s", name)
    db.drop_database(name)