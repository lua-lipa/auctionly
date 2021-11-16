from .. import db
from datetime import datetime
from auctionly.bid.bid import Bid


class Payment(db.Model):

    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer)
    bid_id = db.Column(db.Integer, db.ForeignKey("bid.id"))

    def __init__(self, user_id, auction_id, time, amount, bid_id):
        self.user_id = user_id
        self.auction_id = auction_id
        self.time = time
        self.amount = amount
        self.bid_id = bid_id

    def receive_bid_from_user(user_id, amount, auction_id, highest_bid):
        if (not Payment.able_to_receive_payment(user_id, amount)):
            return False

        # check the highest bid that has been placed on this auction (this is the money we have frozen)
        if (highest_bid != None):
            previous_bid_id = highest_bid.get_bid_id()
            frozen_payment = Payment.query.filter_by(
                bid_id=previous_bid_id).first()

            frozen_payment.unfreeze_payment()

            db.session.flush()
            db.session.commit()

        # freeze the new amount from the new user for this bid and place it into the database
        time = datetime.now()
        bid = Bid(user_id=user_id, auction_id=auction_id,
                  amount=amount, time=time)

        db.session.add(bid)
        db.session.commit()

        new_payment = Payment(
            user_id=user_id, auction_id=auction_id, time=time, amount=amount, bid_id=bid.get_bid_id())

        db.session.add(new_payment)
        db.session.commit()

        print("Succesfully received the bid from the user")
        return True

    def get_time(self):
        return self.time

    def unfreeze_payment(self):
        self.amount = 0

    def able_to_receive_payment(user_id, amount):
        print("checking if the payment of €", str(amount),
              " is able to be received from user ", user_id)
        return True
