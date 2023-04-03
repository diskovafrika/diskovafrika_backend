from flasgger import swag_from
from diskovafrika.models.v1.country import Country
from diskovafrika.repository.v1.country import CountryRepo
from diskovafrika.utils.utils import error_response, custom_response


@swag_from('../../docs/country.yaml')
def get_country(name_capital=None):
    """Returns json object of all countries in DB"""
    resp = {
        'message': "test data",
        'data': f"{name_capital}",
        'status_code': 200
    }
    country = CountryRepo.division(name_capital)
    # print(country)
    # data = {'country': country[0][0], 'administrative_division': country[0][1]}
    # print(data)
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
