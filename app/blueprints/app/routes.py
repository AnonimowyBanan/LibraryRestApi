from flask import jsonify

from . import app


@app.errorhandler(404)
def not_found(message: str) -> jsonify:
    """
    Handle 404 errors.

    This function is triggered when a 404 error occurs in the Flask application.
    It returns a JSON response with a custom error message.

    :param message: The error message to be included in the JSON response.
    :type message: str
    :return: A tuple containing a JSON object with the error message and the HTTP status code 404.
    :rtype: flask.jsonify
    """
    return jsonify({'error': 'Not found', 'message': message}), 404
