import datetime
import json
import logging
import traceback
from flask import Response, jsonify


def error_response(*, message, status_code):
    """
    The error_response function is used to return a JSON response with an error message and status code.
        Args:
            message (str): The error message to be returned in the JSON response.
            status_code (int): The HTTP status code of the response.

    :param *: Pass in a dictionary of parameters
    :param message: Pass the error message to the client
    :param status_code: Set the http status code of the response
    :return: A json object with the following structure:

    """
    if type(message) != dict:
        message = str(message)
    return jsonify(status="error", data=None, message=message), status_code


def custom_response(*, message, data, status_code):
    """
    The custom_response function is a helper function that returns a JSON response with the following format:
    {
        &quot;status&quot;: &quot;success&quot;,
        &quot;message&quot;: message, # A string containing an appropriate success or error message.  This will be displayed to the user.
        &quot;data&quot;: data, # The data returned by your endpoint (if any).  This can be anything from a list of objects to just an integer value.  It's up to you!

    :param *: Pass multiple arguments to the function
    :param message: Pass a message to the user
    :param data: Pass data to the response
    :param status_code: Set the status code of the response
    :return: A response object

    """
    response = {
        "status": "success",
        "message": message,
        "data": data,
    }

    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status_code
    )


def resource_not_found(e):
    """
    The resource_not_found function is a custom error handler that returns a 404 response with the message &quot;URL not be found&quot;.

    :param e: Pass in the error message that is returned from the function
    :return: A 404 error message

    """
    return error_response(message="URL not be found", status_code=404)


def internal_server_error(e):
    """
    The internal_server_error function is a custom error handler that logs the traceback of any errors that occur in the application.
    It also returns an error response with a 500 status code and message.

    :param e: Pass the exception object to the function
    :return: An error response with a status code of 500

    """
    logging.critical(
        f"\n{'='*30} SERVER ERROR {datetime.datetime.now()} {'='*30}\n\n {traceback.format_exc()}\n{'='*24} END SERVER ERROR {'='*24}\n",
    )
    return error_response(message="Internal server error.", status_code=500)
