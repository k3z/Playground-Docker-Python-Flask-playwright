import os
from flask import Flask
from flask_cors import CORS


def create_app(config="api/config.py"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(os.path.join(os.getcwd(), config))

    cors = CORS()
    cors.init_app(app)

    # Blueprints
    with app.app_context():
        from api.views.public import bp_public
        from api.views.api_private import api_private
        from api.cli.app import bp as cli_app

        app.register_blueprint(bp_public)
        app.register_blueprint(api_private)
        app.register_blueprint(cli_app)

    return app
