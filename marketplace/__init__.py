from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    ##### DATABASE #####

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    db.init_app(app)


    ###### LOGIN #####

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import tools
    app.register_blueprint(tools.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import views
    bootstrap = Bootstrap(app)
    app.register_blueprint(views.bp)
    
    app.secret_key = "the80sselfhelpguru"

    from . import userdash
    app.register_blueprint(userdash.bp)


    @app.errorhandler(404)
    def not_found(e):
        heading = "404"
        image = "../static/img/404.png"

        return render_template("error.html", heading=heading, image=image), 404

    @app.errorhandler(500)
    def server_error(e):
        heading = "500, Internal Server Error"
        image = "../static/img/500.png"
        return render_template("error.html", heading=heading, image=image), 500

    UPLOAD_FOLDER = "../static/img"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    return app
