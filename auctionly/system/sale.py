from .. import db

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sold_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    bought_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))

    def __init__(self, seller_id, buyer_id, auction_id):
        self.sold_by = seller_id
        self.bought_by = buyer_id
        self.auction_id = auction_id

    def get_sold_by(self):
        return self.sold_by

    def get_bought_by(self):
        return self.bought_by
    
