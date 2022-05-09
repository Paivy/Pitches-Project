# from ensurepip import bootstrap
from trace import Trace
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initializing application
app = Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

#Initializing Flask extensions
bootstrap = Bootstrap(app)


from app import views