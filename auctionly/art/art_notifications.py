from auctionly import db

class Art_Notifications(db.Model):
    """Art notification class implemented to create art notification"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_id = db.Column(db.Integer, db.ForeignKey("art.id"))

    def __init__(self, user_id, art_id):
        self.user_id = user_id
        self.art_id = art_id

    def get_art_id(self):
        return self.art_id
