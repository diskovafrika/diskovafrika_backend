from flask import Blueprint
from diskovafrika.controllers.v1.country import country_div, get_country, all_countries

country_bp = Blueprint("country", __name__)

country_bp.get("/")(all_countries)
country_bp.get("/details")(get_country)
country_bp.get("/administrative-division/<country>")(country_div)
# country_bp.get("/yoi/<country>")(country_div)
# country_bp.get("/region/<country>")(country_region)
