from flask import Flask, jsonify

# from flask_cors import CORS

from src import api
from config import DevelopmentConfig, TestingConfig
from marshmallow import ValidationError
from extensions import db, ma


def create_app(test_config=False):
    """Create a new app instance."""

    my_app = Flask(__name__)
    my_app.config.from_object(DevelopmentConfig())

    if test_config is False:
        # load the instance config, if it exists, when not testing
        my_app.config.from_object(DevelopmentConfig())
    else:
        # load the test config if passed in
        my_app.config.from_object(TestingConfig())

    api.init_app(my_app)
    db.init_app(my_app)
    db.app = my_app
    ma.init_app(my_app)

    return my_app


app = create_app()
db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


# @pytest.fixture
if __name__ == "__main__":
    app.run(
        port=5000, use_reloader=False
    )  # use_reloader is added so that the apscheduler doesn't execute twice
