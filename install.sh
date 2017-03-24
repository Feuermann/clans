#!/usr/bin/env bash
#
#   At first write database config file in  app/etc/config/settings.conf
#
echo "Install required packages"

sudo apt-get update
sudo apt-get install build-essential python-pip libffi-dev python-dev python3-dev libpq-dev

type virtualenv >/dev/null 2>&1 || { echo >&2 "No suitable python virtual env tool found, aborting"; exit 1; }

rm -rf .venv

# create virtual environment
virtualenv -p python3 .venv

# activate virtual environment
source .venv/bin/activate

# install required python packages
pip install -r requirement.txt

# update alembic config
python3 install.py

# create alembic migration to database
alembic upgrade head
