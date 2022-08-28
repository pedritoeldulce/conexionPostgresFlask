from flask import Flask
from .views import page


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(page)

    return app
