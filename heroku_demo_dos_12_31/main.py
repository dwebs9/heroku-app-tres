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
from flask_sqlalchemy import SQLAlchemy

from marketplace import __init__
from marketplace import create_app



if __name__ == "__main__":
    app = create_app()
    app.run()


