"""
Copyright (c) 2023 - present diskovafrika.com
"""
import os
from flask import Flask
from flask_cors import CORS, cross_origin
from diskovafrika.configs.config import configs
from flasgger import Swagger
from diskovafrika.models import User
from diskovafrika.routes import home, user_bp, country_bp
from diskovafrika.utils.utils import resource_not_found, internal_server_error
from diskovafrika.configs.extensions import db, init_app
from diskovafrika.configs.swagger import template, swagger_config


def create_app():
    """
    The create_app function is the main entry point for our application.
    It creates a Flask app instance and configures it with the settings found in
    the environment variable ENVIRONMENT, which can be either 'development' or 'production'.
    The function also registers blueprints (which are like mini-apps) to handle different parts of our API.
    :return: The app variable
    """
    environ = os.getenv("ENVIRONMENT")
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/v1*": {"origins": "*"}})
    app.config.from_object(configs.get(environ))
    Swagger(app, config=swagger_config, template=template)
    db.app = app
    init_app(app)
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')
    app.register_blueprint(country_bp, url_prefix='/api/v1/country')
    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(500, internal_server_error)

    return app
