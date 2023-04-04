from flasgger import swag_from
from flask import request
from diskovafrika.models.v1.country import Country
from diskovafrika.repository.v1.country import CountryRepo
from diskovafrika.utils.utils import error_response, custom_response


@swag_from('../../docs/country_details.yaml')
def get_country():
    """Returns detailed information of a country"""
    name = request.args.get('name')
    capital = request.args.get('capital')
    yoi = request.args.get('yoi')
    region = request.args.get('region')
    if yoi is not None:
        countries_by_year = CountryRepo.get_country_by_yoi(yoi=yoi)
        return countries_by_year
    elif region:
        countries_by_region = CountryRepo.get_country_by_region(region=region)
        return countries_by_region
    else:
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
