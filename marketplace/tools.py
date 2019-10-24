import datetime
from flask import (Blueprint, flash, render_template, session,
                   request, url_for, redirect)
from .models import Tool
from .forms import CreateForm
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import secure_filename
from decimal import Decimal, getcontext
import os
from . import db


bp = Blueprint('tool', __name__, url_prefix='/tools')

def check_upload_file(form):
    # get file data from form
    fp = form.images.data
    filename = fp.filename
    # get the current path of the module file… store file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, "static/img", secure_filename(filename))
    # store relative path in DB as image location in HTML is relative
    db_upload_path = "/static/img/" + secure_filename(filename)
    # save the file and return the db upload path
    fp.save(upload_path)

    return db_upload_path


@bp.route("/create", methods=["GET", "POST"])
def create():
    form = CreateForm()
    heading = "List an Item"
    if form.validate_on_submit():
        print("Form validated")
        db_file_path = check_upload_file(form)
        new_tool = Tool(
            images=db_file_path,
            tool_name=form.tool_name.data,
            modelNo=form.modelNo.data,
            list_price=form.list_price.data,
            category=form.category.data,
            user_id=1,
            desc=form.desc.data,
            brand=form.brand.data,
        )
        db.session.add(new_tool)

        db.session.commit()
        return redirect(url_for("tool.create"))

    return render_template("tools/create.html", form=form, heading=heading)