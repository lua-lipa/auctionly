""" User class implemented to provide parent class methods to its children """
from flask_login import UserMixin
from .. import db
from auctionly.art.art import Art


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.feed = []

    def get_user_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        # to-do: implement hashing function for password
        pass

    # As a seller I want to be able to view the feed so that I can see the art available.
    def get_user_feed(self):
        return self.feed

    def set_user_feed(self, feed):
        self.feed = feed

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_art(self):
        return Art.query.filter_by(owner_id=self.id).all()
