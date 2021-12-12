""" handles the creation and placement of bids """
from datetime import datetime
from .. import db


class Bid(db.Model):
    """ this is a class that creates a bid object, it is connected to SQLAlchemy """
    __tablename__ = 'bid'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer)

    def __init__(self, auction_id, time, user_id, amount):
        """creates a bid object"""
        self.auction_id = auction_id
        self.time = time
        self.user_id = user_id
        self.amount = amount

    def get_user_id(self):
        """ returns the user id of the user who placed the bid """
        return self.user_id

    def get_amount(self):
        """ returns the bidding amount """
        return self.amount

    def get_time(self):
        """ returns the bidding time """
        return self.time

    def get_bid_id(self):
        """ returns the bid id """
        return self.id
