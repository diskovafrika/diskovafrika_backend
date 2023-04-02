#!/usr/bin/env bash

# Tell Flask where is our app
export FLASK_APP=run.py
# track changes
flask db init
# run migrations
flask db migrate -m"initial migration"
# apply migrations
flask db upgrade
