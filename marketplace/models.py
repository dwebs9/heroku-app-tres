from . import db
from datetime import datetime
from flask_login import UserMixin


class Tool(db.Model):
    __tablename__ = "tools"
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100))
    modelNo = db.Column(db.String(100))
    list_price = db.Column(db.Float(100))
    category = db.Column(db.String(100))
    user_id = db.Column(db.Integer default="non_user")
    desc = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now())
    sold_status = db.Column(db.String(100), default="")
    images = db.Column(db.String(1000), default='noimage.png')

    # bid_id = db.relationship('Bid', backref='tools')
