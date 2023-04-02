from flasgger import swag_from
from diskovafrika.models.v1.country import Country
from diskovafrika.utils.utils import error_response, custom_response


@swag_from('../../docs/country.yaml')
def get_country(name_capital=None):
    """Returns json object of all countries in DB"""
    resp = {
        'message': "test data",
        'data': f"{name_capital}",
        'status_code': 200
    }
    return custom_response(**resp)


def all_countries():
    resp = {
        'message': "endpoint working",
        'data': "Test data",
        'status_code': 200
    }

    return custom_response(**resp)
