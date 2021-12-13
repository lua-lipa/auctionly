""" User class implemented to provide parent class methods to its children """
from flask_login import UserMixin
from auctionly.art.art import Art
from auctionly.art.art_notifications import ArtNotifications
from auctionly.users.user_preference import User_Preference
from .. import db


class User(db.Model, UserMixin):
    """ initializing the user class and providing getters and setters to
    interact with the users model in the database.  """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    user_type = db.Column(db.String)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.feed = []

    def get_user_id(self):
        """ returns the id of the user """
        return self.id

    def get_name(self):
        """ returns the name of the user """
        return self.first_name

    def get_last_name(self):
        """ returns the last name of the user """
        return self.last_name

    def get_full_name(self):
        """ returns the full name of the user """
        return self.first_name + " " + self.last_name

    def get_email(self):
        """ returns the email of the user """
        return self.email

    def get_password(self):
        """ returns the hashed password of the user """
        # to-do: implement hashing function for password
        return self.password

    # As a seller I want to be able to view the feed so that I can see the art available.
    def get_user_feed(self):
        """ returns the feed of the user """
        return self.feed

    def get_user_art(self):
        """ returns the art uploaded of the user """
        return Art.query.filter_by(owner_id=self.id).all()

    def get_user_prefs(self):
        """ returns the preferences of the user """
        user_pref = User_Preference.query.filter_by(user_id=self.id).all()
        prefs = []
        for pref in user_pref:
            prefs.append(pref.get_name())
        return prefs

    def get_auction_notification_list(self):
        """ returns the notifications of the user """
        user_subs = ArtNotifications.query.filter_by(user_id=self.id).all()
        user_notifications = []
        for sub in user_subs:
            art_id = sub.get_art_id()
            print("art_id")
            print(art_id)
            art = Art.query.filter_by(id=art_id).first()
            if art.get_up_for_auction() == "True":
                user_notifications.append(art)
        return user_notifications

    def get_notification_list(self):
        """ returns the list of notifications of the user """
        user_subs = ArtNotifications.query.filter_by(user_id=self.id).all()
        subs_ids = []
        for sub in user_subs:
            art_id = sub.get_art_id()
            subs_ids.append(art_id)
        return subs_ids

    def get_user_type(self):
        """ returns the type of the user """
        return self.user_type
