from insta import db, login_manager
from flask_login import UserMixin
from datetime import datetime as dt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    image_file = db.Column(db.String(120), default='default.jpg')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baseurl = db.Column(db.String(60))
    url = db.Column(db.String(60))
    date_uploaded = db.Column(db.DateTime, default=dt.utcnow())
    owner = db.Column(db.String(60))
    likes = db.Column(db.Integer)
    caption = db.Column(db.String(60), default="")
    tags = db.Column(db.Integer, default=0)
    main_colour = db.Column(db.String(60), default="")
