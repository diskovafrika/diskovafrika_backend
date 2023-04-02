from flask import Blueprint
from diskovafrika.controllers.v1.country import get_country, all_countries

country_bp = Blueprint("country", __name__)

country_bp.get("/")(all_countries)
country_bp.get("/<name_capital>")(get_country)
