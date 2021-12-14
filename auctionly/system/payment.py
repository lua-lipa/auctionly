""" payment system handles receiving, freezing and
sending money through our system """
from datetime import datetime
from auctionly import fee_constants
from ..bid.bid import Bid
from .. import db


class Payment(db.Model):
    """this class handles receiving, freezing and sending money through our system"""

    __tablename__ = "payment"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer)
    bid_id = db.Column(db.Integer, db.ForeignKey("bid.id"))
    seller_paid = db.Column(db.Integer)
    service_fee_paid = db.Column(db.Integer)

    def __init__(
        self,
        user_id,
        auction_id,
        time,
        amount,
        bid_id,
        seller_paid=0,
        service_fee_paid=0,
    ):
        self.user_id = user_id
        self.auction_id = auction_id
        self.time = time
        self.amount = amount
        self.bid_id = bid_id
        self.seller_paid = seller_paid
        self.service_fee_paid = service_fee_paid

    def receive_bid_from_user(self, user_id, amount, auction_id, highest_bid):
        """receives bid from user, updates the database"""
        if not self.able_to_receive_payment(user_id, amount):
            return False

        # check the highest bid that has been placed on this auction
        # (this is the money we have frozen)
        if highest_bid is not None:
            previous_bid_id = highest_bid.get_bid_id()
            frozen_payment = self.query.filter_by(
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
            user_id=user_id,
            auction_id=auction_id,
            time=time,
            amount=amount,
            bid_id=bid.get_bid_id(),
        )

        db.session.add(new_payment)
        db.session.commit()

        print("Succesfully received the bid from the user")
        return True

    def get_amount(self):
        """get amount of payment"""
        return self.get_amount()

    def get_time(self):
        """get time of payment"""
        return self.time

    def unfreeze_payment(self):
        """unfreeze a payment placed by the user"""
        self.amount = 0

    def able_to_receive_payment(self, user_id, amount):
        """check that the buyer is able to pay for the bidding"""
        print(
            "checking if the payment of €",
            str(amount),
            " is able to be received from user ",
            user_id,
        )
        return True

    def pay_insurance_fee(self, auction):
        """send the fee needed for authentication"""
        insurance_fee_fraction = fee_constants.AUTHENTICATION_FEE_FRACTION

        # fetch the bid that has been placed on the auction
        payment = self.query.filter_by(
            auction_id=auction.get_auction_id).first()

        if payment is not None:
            amount_bidder_pays = payment.get_amount()
            amount_paid_for_service = amount_bidder_pays * insurance_fee_fraction
            amount_taken_from_seller = amount_bidder_pays - amount_paid_for_service

            payment.seller_paid = amount_taken_from_seller
            payment.service_fee_paid = amount_paid_for_service

            db.session.commit()

    def pay_seller(self, auction):
        """send the money placed by the bidder to the seller"""
        service_fee_fraction = fee_constants.AUCTION_FEE_FRACTION
        insurance_fee_fraction = fee_constants.AUCTION_FEE_FRACTION

        # fetch the bid that has been placed on the auction
        payment = self.query.filter_by(
            auction_id=auction.get_auction_id).first()

        if payment is not None:
            amount_bidder_pays = payment.get_amount()
            amount_paid_for_service = amount_bidder_pays * service_fee_fraction
            amount_paid_for_insurance = amount_bidder_pays * insurance_fee_fraction
            amount_paid_to_seller = amount_bidder_pays - (amount_paid_for_service + amount_paid_for_insurance)

            payment.seller_paid = amount_paid_to_seller
            payment.service_fee_paid = amount_paid_for_service

            db.session.commit()
