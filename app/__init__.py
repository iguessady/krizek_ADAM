from flask import Flask
from config import Config


def create_app(config_class=Config):
    # vytvorí a nastaví Flask aplikáciu
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route("/")
    def index():
        return "Hello ADAM"

    return app