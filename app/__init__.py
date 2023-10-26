from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 

# Create an instance of the Flask class
app = Flask(__name__)
# Configure our app with the Attributes and Values from the Config class
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to track our database migrations
migrate = Migrate(app, db)
# create an instance of migrate to handle auth
login = LoginManager(app)
login.login_view = 'login'

#regist the api blueprint with out app
from app.blueprints.api import api
app.register_blueprint(api)

from . import routes, models
