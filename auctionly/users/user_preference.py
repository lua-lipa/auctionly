from .. import db
from .user import User

class User_Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_pref = db.Column(db.String(150))

    def __init__(self, user_id, art_pref):
        """creates an art object"""
        self.user_id = user_id
        self.art_pref = art_pref

    def get_user_art_pref(self, u_id):
        return User_Preference.query.filter_by(user_id=u_id).all()
