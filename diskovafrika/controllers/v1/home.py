from diskovafrika.utils.utils import custom_response


def api_status():
    """
    The api_status function returns a custom_response object with the following attributes:
        message: &quot;Running...&quot;,
        data: &quot;Welcome to DiskovAfrika&quot;,
        status_code: 200

    :return: A custom response with the status code 200 and a message

    """
    resp = {
        'message': "Running...",
        'data': "Welcome to DiskovAfrika",
        'status_code': 200
    }
    return custom_response(**resp)
