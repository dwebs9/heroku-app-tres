from flask import Blueprint, flash, render_template, request, , redirect
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
from .models import Tool
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from . import db

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
    search_results = []
    print("########## attempt to submit form")
    if search.validate_on_submit():

        search_string = search.data["search"]
        # print(search_string)
        if search_string != "":
            all_tools = Tool.query.all()
            print(all_tools[0].tool_name)
            for tool in all_tools:
                if re.search(search_string, tool.tool_name, re.IGNORECASE):
                    print("########## Underneath this lies the search results")
                    print(search_results)
                    search_results.append(tool)
        else:
            print("This string is empty")

        return render_template("results.html", form=search, items=search_results)

    return render_template("results.html", form=search)
