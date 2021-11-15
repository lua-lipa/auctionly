from auctionly import db
import datetime

class Auction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_id = db.Column(db.Integer, db.ForeignKey("art.id"))
    description = db.Column(db.String(150))
    starter_price = db.Column(db.String(150))
    bid_increment = db.Column(db.String(150))
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, end_time, seller_id, art_id, 
    auction_description, starter_price, bid_increment):
    # auction_description, starter_price, bid_increment, auction_type, sold, buyer_id, bids, payment):
        self.end_time = end_time
        self.seller_id = seller_id
        self.art_id = art_id
        self.auction_description = auction_description
        self.starter_price = starter_price
        self.bid_increment = bid_increment
        # self.auction_type = auction_type
        # self.sold = sold
        # self.buyer_id = buyer_id
        # self.bids = bids
        # self.payment = payment

    def get_upload_time(self):
        return self.upload_time
    
    def get_end_time(self):
        return self.end_time

    def get_seller_id(self):
        return self.seller_id
    
    def get_auction_id(self):
        return self.auction_type
        
    def get_art_id(self):
        return self.art_id
    
    def get_auction_description(self):
        return self.auction_description
    
    def get_starter_price(self):
        return self.starter_price
    
    def get_bid_increment(self):
        return self.bid_increment
    
    def get_auction_type(self):
        return self.auction_type
    
    def get_sold(self):
        return self.sold
    
    def get_buyer_id(self):
        return self.buyer_id
    
    def get_bids(self):
        return self.bids
    
    def get_payment(self):
        return self.payment

    def set_auction_description(self, auction_description):
        self.auction_description = auction_description
    
    def set_starter_price(self, starter_price):
        self.starter_price = starter_price
    
    def set_bid_increment(self, bid_increment):
        self.bid_increment = bid_increment
    
    def set_sold(self, sold):
        self.sold = sold
    
    def set_buyer_id(self, buyer_id):
        self.buyer_id = buyer_id
    
    def set_bids(self, bids):
        self.bids = bids
    
    def set_payment(self, payment):
        self.payment = payment

    
