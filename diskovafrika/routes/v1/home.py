from flask import Blueprint
from diskovafrika.controllers.v1.home import api_status

home = Blueprint("home", __name__)

home.get("/")(api_status)
