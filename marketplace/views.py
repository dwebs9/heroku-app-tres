from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_login import login_required
from flask import session as login_session
from flask import session
from sqlalchemy import desc
import sqlalchemy as db
import os
from werkzeug.utils import secure_filename
import re
from flask_table import Table, Col
from flask import Flask, render_template
from flask_bootstrap import *
from .forms import LandingForm, SearchForm
from flask_sqlalchemy import SQLAlchemy


bp = Blueprint("app", __name__)

@bp.route('/', methods=["GET", "POST"])
def index():
    form_land = LandingForm()
    if request.args.get("landing_search") != None:
        print("Form has validated")


    return render_template("index.html", form=form_land)



@bp.route("/results", methods=["GET", "POST"])
def search():

    search = SearchForm()

    if search.validate_on_submit():
        print("The eagle has landed AKA the form has submitted")



    return render_template("results.html", form=search)
