import os
import sys
import configparser

ALEMBIC = "alembic.ini"

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'app','etc','config','settings.conf')

DB_CONF = configparser.SafeConfigParser()

DB_CONF.read(DB_FILE)
POSTGRES = DB_CONF['database']
DB_CONFIG = (POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['database'])
DATABASE_URL = "postgresql://%s:%s@%s/%s" % DB_CONFIG

DB_CONF.read(ALEMBIC)
DB_CONF['alembic']['sqlalchemy.url'] = DATABASE_URL

with open(ALEMBIC, 'w') as file:
    DB_CONF.write(file)
