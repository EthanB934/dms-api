#!/bin/bash

rm db.sqlite3
rm -rf ./dms/migrations
python3 manage.py makemigrations dmsapp
python3 manage.py migrate
python3 manage.py loaddata storeasusers
python3 manage.py loaddata tokens
python3 manage.py loaddata types


