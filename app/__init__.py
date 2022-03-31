from flask import Flask
from config import Production
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Production)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import routes, models, admin
