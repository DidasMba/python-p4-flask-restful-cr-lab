# server/app.py

from flask import Flask
from .models import db
from .controllers import get_plants, get_plant, create_plant

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"
db.init_app(app)

app.route("/plants", methods=["GET"])(get_plants)
app.route("/plants/<int:id>", methods=["GET"])(get_plant)
app.route("/plants", methods=["POST"])(create_plant)

