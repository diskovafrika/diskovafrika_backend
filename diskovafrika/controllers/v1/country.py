from flasgger import swag_from
from flask import request
from diskovafrika.models.v1.country import Country
from diskovafrika.repository.v1.country import CountryRepo
from diskovafrika.utils.utils import error_response, custom_response


@swag_from('../../docs/country.yaml')
def get_country():
    """Returns json object of all countries in DB"""
    name = None
    capital = None

    name = request.args.get('name')
    capital = request.args.get('capital')
    # print(capital)
    country = CountryRepo.get_country(name=name, div=capital)
    return country


@swag_from('../../docs/country_all.yaml')
def all_countries():
    all_country = CountryRepo.all()
    return all_country, 200


@swag_from('../../docs/country_division.yaml')
def country_div(country):
    """Returns the administrative division type of a country"""
    country_div_res = CountryRepo.division(country)
    return country_div_res
