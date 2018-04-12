from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


# initialize bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    # create app instance
    app = Flask(__name__)

    # app configurations
    app.config.from_object(config_options[config_name])

    # initialize bootstrap extension instance in app
    bootstrap.init_app(app)

    # register bluprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
