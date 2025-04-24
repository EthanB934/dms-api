#!/bin/bash

rm db.sqlite3
rm -rf ./dms/migrations
python3 manage.py makemigrations dmsapp
python3 manage.py migrate dmsapp



