from .. import db
from datetime import datetime


class Bid(db.Model):

    __tablename__ = 'bid'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, auction_id, time, user_id):
        """creates a bid object"""
        self.id = id
        self.auction_id = auction_id
        self.time = time
        self.user_id = user_id
