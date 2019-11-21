from flask import Flask

from .extensions import all_extensions
from .blueprints.kjv_api_v1.views import api_v1

def create_app(config: dict = None):
    '''Create a Flask application using the app factory pattern.

    Args:
      config (dict): Configuration dictionary for Flask application

    Returns: Flask app (Flask)

    '''
    # Create the Flask app

    # Configure the flask app with the following values:
    # - SQLALCHEMY_DATABASE_URI : 'sqlite:////kjv/kjv.db'
    # - SQLALCHEMY_TRACK_MODIFICATIONS : False

    # If the config parameter is not None:
    #   app.config.update(config)

    # Register the api_v1 Blueprint

    init_extensions(app)

    return app
    

def init_extensions(app: Flask):
    '''Register extensions. This will change (mutate) the app passed in.

    Args:
      app (Flask): Flask application instance

    Returns: None

    '''
    for extension in all_extensions():
        extension.init_app(app)
