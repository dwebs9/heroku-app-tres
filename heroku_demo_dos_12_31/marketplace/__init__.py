from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    from . import views
    bootstrap = Bootstrap(app)
    app.register_blueprint(views.app)
    return app
