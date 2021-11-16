from .. import db

class User_Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_pref = db.Column(db.String(150))

    def __init__(self, user_id, art_pref):
        """creates an art object"""
        self.user_id = user_id
        self.art_pref = art_pref
    
    def get_name(self):
        return self.art_pref
