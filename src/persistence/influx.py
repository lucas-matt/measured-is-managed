import os
from influxdb import InfluxDBClient

def read_env():
    """
    Read environment variables for database details
    """
    environ = os.environ
    host = environ.get('DBHOST', 'localhost')
    port = int(environ.get('DBPORT', '8086'))
    user = environ.get('DBUSER', 'username')
    password = environ.get('DBPASS', 'password')
    db = environ.get('DBNAME', 'db')
    return (host, port, user, password, db)

def create_client(creds_tuple=read_env()):
    return InfluxDBClient(creds_tuple)

