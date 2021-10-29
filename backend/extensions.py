import logging
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging

ma = Marshmallow()
db = SQLAlchemy()

logger = logging.getLogger("Program logger")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler = logging.FileHandler("./api_logging.log")
handler.setFormatter(formatter)
logger.addHandler(handler)
