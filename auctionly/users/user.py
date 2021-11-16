""" User class implemented to provide parent class methods to its children """
from flask_login import UserMixin
from .. import db
from auctionly.art.art import Art
from auctionly.art.art_notifications import Art_Notifications
from auctionly.users.user_preference import User_Preference


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

    def get_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

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
    
    def get_user_prefs(self):
        user_pref = User_Preference.query.filter_by(user_id=self.id).all()
        prefs = []
        for pref in user_pref:
            prefs.append(pref.get_name())
        return prefs
    
    def get_auction_notification_list(self):
        user_subs = Art_Notifications.query.filter_by(user_id=self.id).all()
        user_notifications = []
        for sub in user_subs:
            art_id = sub.get_art_id()
            print("art_id")
            print(art_id)
            art = Art.query.filter_by(id=art_id).first()
            if(art.get_up_for_auction() == "True"):
                user_notifications.append(art)
        return user_notifications
    
    def get_notification_list(self):
        user_subs = Art_Notifications.query.filter_by(user_id=self.id).all()
        subs_ids = []
        for sub in user_subs:
            art_id = sub.get_art_id()
            subs_ids.append(art_id)
        return subs_ids
