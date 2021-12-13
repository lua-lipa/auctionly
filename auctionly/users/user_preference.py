"""module to hold the user preference class"""
# pylint: disable=E0402
from .. import db

class UserPreference(db.Model):
    """class to create the user_preference table in database"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_pref = db.Column(db.String(150))

    def __init__(self, user_id, art_pref):
        """creates an art object"""
        self.user_id = user_id
        self.art_pref = art_pref

    def get_name(self):
        """returns the name of the art prefernece"""
        return self.art_pref

    def get_user_id(self):
        """returns the id associated with this art preference object"""
        return self.user_id
