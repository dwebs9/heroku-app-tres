import datetime
from flask import (Blueprint, flash, render_template, session,
                   request, url_for, redirect)
from .models import Tool, Bid, User
from .forms import BidForm, MarkSold, UndoSold, CreateForm
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import secure_filename
from decimal import Decimal, getcontext
import os


bp = Blueprint('tool', __name__, url_prefix='/tools')



@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = CreateForm()
    heading = "List an Item"
    if form.validate_on_submit():
        print("Form validated")
        db_file_path = check_upload_file(form)
        new_tool = Tool(
            images=db_file_path,
            tool_name=form.title.data,
            modelNo=form.modelNo.data,
            list_price=form.price.data,
            category=form.category.data,
            user_id=session.get("user_id"),
            desc=form.description.data,
            brand=form.brand.data,
        )
        db.session.add(new_tool)

        db.session.commit()
        return redirect(url_for("tool.create"))

    return render_template("tools/create.html", form=form, heading=heading)