from flask import Flask, jsonify

# from flask_cors import CORS

from src import api
from config import DevelopmentConfig
from marshmallow import ValidationError
from extensions import db, ma


def create_app():
    """Create a new app instance."""

    my_app = Flask(__name__)
    my_app.config.from_object(DevelopmentConfig())

    api.init_app(my_app)
    db.init_app(my_app)
    db.app = my_app
    ma.init_app(my_app)

    # with my_app.app_context():
    #     """
    #     The application context keeps track of the application-level data during a request,
    #     CLI command, or other activity.
    #     Rather than passing the application around to each function

    #     """
    #     # load cron jobs
    #     from apis.cron import user_loading

    #     scheduler.init_app(my_app)
    #     scheduler.start()

    return my_app


# bind_key = 'smf'
app = create_app()
# cors = CORS(app, resources={r"*": {"origins": "*"}})
db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


if __name__ == "__main__":
    app.run(
        port=5000, use_reloader=False
    )  # use_reloader is added so that the apscheduler doesn't execute twice
