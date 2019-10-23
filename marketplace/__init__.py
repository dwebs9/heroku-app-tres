from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    ##### DATABASE #####

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    db.init_app(app)

    from . import tools
    app.register_blueprint(tools.bp)




    from . import views
    bootstrap = Bootstrap(app)
    app.register_blueprint(views.bp)
    app.secret_key = "the80sselfhelpguru"
    return app
