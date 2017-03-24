#!/usr/bin/env bash

source .venv/bin/activate
gunicorn -b 127.0.0.1:5050 --reload app.main:application