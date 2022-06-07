#!/bin/bash
chmod +x
flaskr/util/createdb.py

python -m flask run --host=0.0.0.0

python ./flaskr/util/createdb.py