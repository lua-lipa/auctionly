"""Art notification module implemented to hold Art Notifications class"""
from ..auctionly import db

class ArtNotifications(db.Model):
    """Art notification class implemented to create art notification"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_id = db.Column(db.Integer, db.ForeignKey("art.id"))

    def __init__(self, user_id, art_id):
        """creates an art notification object/row in the table"""
        self.user_id = user_id
        self.art_id = art_id

    def get_art_id(self):
        """returns the art id of a row in a table"""
        return self.art_id

    def get_art_user_id(self):
        """returns the art id of a row in a table"""
        return self.art_id
