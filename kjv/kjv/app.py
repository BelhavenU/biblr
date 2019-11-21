from flask import Flask

from .extensions import all_extensions
from .blueprints.kjv_api_v1.views import api_v1

def create_app(config: dict = None):
    '''Create a Flask application using the app factory pattern.

    Args:
      config (dict): Configuration dictionary for Flask application

    Returns: Flask app (Flask)

    '''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////kjv/kjv.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if config:
        app.config.update(config)

    app.register_blueprint(api_v1)

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
