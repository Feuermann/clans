import os
import configparser
import falcon
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# path to app dir
APP_DIR = os.path.abspath(os.path.dirname(__file__))

# path to work directory
WORK_DIR = os.path.dirname(APP_DIR)

# path to configuration file
CONF_FILE = os.path.join(APP_DIR, 'etc', 'config', 'settings.conf')

SQL_PATH = os.path.join(APP_DIR, 'etc', 'database')

CONFIG = configparser.ConfigParser()
CONFIG.read(CONF_FILE)
DATABASE = CONFIG['database']
DB_AUTOCOMMIT = True


DB_CONFIG = (DATABASE['user'], DATABASE['password'], DATABASE['host'], DATABASE['database'])
DATABASE_URL = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG
DATABASE_OPTION = {
    'pool_recycle': 3600,
    'pool_size': 10,
    'pool_timeout': 30,
    'max_overflow': 30,
    'execution_options': {
        'autocommit': DB_AUTOCOMMIT
    }
}


ENGINE = create_engine(DATABASE_URL, **DATABASE_OPTION)
SESSION = scoped_session(sessionmaker())


def session_init():
    SESSION.configure(bind=ENGINE)
    from app.models.user import Base
    Base.metadata.create_all(ENGINE)

