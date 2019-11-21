from flask import Flask

from .blueprints.page.views import page
from .blueprints.bible.views import bible

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(page)
    app.register_blueprint(bible)

    return app
