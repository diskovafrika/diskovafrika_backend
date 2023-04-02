from diskovafrika.utils.utils import custom_response


def api_status():
    resp = {
        'message': "Running...",
        'data': "Welcome to DiskovAfrika",
        'status_code': 200
    }
    return custom_response(**resp)
