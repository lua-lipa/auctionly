""" this file holds the auction class which handles the auctioning process """
from auctionly.bid.bidcollection import BidIterator
import datetime
from auctionly import db
from auctionly.bid.bid import Bid
from auctionly.art.art import Art
from auctionly.system.shipment import Shipment
from auctionly.system.authentication import Authentication
from auctionly.users.user import User
from auctionly.system.payment import Payment
from auctionly.auction.auction_state import *


class Auction(db.Model):
    """this class handles the auctioning process, everything from setting up an auction
    to placing a bid on an auction and finalizing an auction."""

    id = db.Column(db.Integer, primary_key=True)
    end_time = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_id = db.Column(db.Integer, db.ForeignKey("art.id"))
    description = db.Column(db.String(150))
    starter_price = db.Column(db.String(150))
    bid_increment = db.Column(db.String(150))
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(
        self, end_time, seller_id, art_id, description, starter_price, bid_increment
    ):
        self.end_time = end_time
        self.seller_id = seller_id
        self.art_id = art_id
        self.auction_description = description
        self.starter_price = starter_price
        self.bid_increment = bid_increment
        self.buyer_id = None
        self.payment = None
        self.state = Started()

    def get_upload_time(self):
        """return upload time"""
        return self.upload_time

    def get_end_time(self):
        """return finish time"""
        return self.end_time

    def get_seller_id(self):
        """return auction seller id"""
        return self.seller_id

    def get_auction_id(self):
        """return auction id"""
        return self.id

    def get_art_id(self):
        """return auction art id"""
        return self.art_id

    def get_auction_description(self):
        """return auction art id"""
        return self.description

    def get_starter_price(self):
        """return auction art id"""
        return self.starter_price

    def get_bid_increment(self):
        """return auction art id"""
        return self.bid_increment

    def get_auction_type(self):
        """return auction art id"""
        return self.auction_type

    def get_sold(self):
        """return whether item is sold"""
        return self.sold

    def get_buyer_id(self):
        """return the id of a buyer"""
        return self.buyer_id

    def get_payment(self):
        """return auction art the payment that was placed on sale"""
        return self.payment

    def get_state(self):
        """return auction art the payment that was placed on sale"""
        return self.state

    def set_auction_description(self, description):
        """return auction description"""
        self.description = description

    def set_starter_price(self, starter_price):
        """return auction starting price"""
        self.starter_price = starter_price

    def set_bid_increment(self, bid_increment):
        """return auction bid increment"""
        self.bid_increment = bid_increment

    def set_buyer_id(self, buyer_id):
        """set buyer for the auction"""
        self.buyer_id = buyer_id

    def set_payment(self, payment):
        """set payment for the auction"""
        self.payment = payment

    def set_state(self, state):
        self.state = state

    def get_time_since_start(self):
        """displays how much time has passed since the beginning of the auction"""
        now = datetime.datetime.now()
        return now - self.get_upload_time()

    def get_time_left(self):
        """returns how much time is left before the auction ends
        by default it is set to last 3 days since the start of the auction"""
        # time_out = self.get_upload_time() + datetime.timedelta(days=3)
        time_out = self.get_end_time()
        now = datetime.datetime.now()
        if now >= time_out:
            return 0
        return time_out - now

    def get_bids(self):
        """return bids placed on the auction by querying the db"""
        return Bid.query.filter_by(auction_id=self.get_auction_id()).all()

    def get_highest_bid(self):
        """returns the BID object of the highest bid"""
        if self.get_number_of_bids() == 0:
            return None

        bids = self.get_bids()
        highest_bid_amount = int(self.get_starter_price())
        highest_bid = None
        for bid in bids:
            if bid.get_amount() >= highest_bid_amount:
                highest_bid_amount = bid.get_amount()
                highest_bid = bid

        return highest_bid

    def get_latest_bid(self):
        """returns the HIGHEST BIDDING AMOUNT placed on the item"""
        highest_bid = self.get_highest_bid()
        if highest_bid is None:
            return 0
        return highest_bid.get_amount()

    def get_current_bidding_price(self):
        """return current bidding price of the auction"""
        if len(self.get_bids()) == 0:
            return self.get_starter_price()
        latest_bid = self.get_latest_bid()
        return int(latest_bid) + int(self.get_bid_increment())

    def get_number_of_bids(self):
        """return number of bids the auction has"""
        return len(self.get_bids())

    def get_title(self):
        """return the title of the auction"""
        art = Art.query.filter_by(id=self.get_art_id()).one()
        return art.get_name()

    def place_bid(self, user_id):
        """place a bid on the auction from the input user"""
        # get the amount of the next bid to be placed
        amount = self.get_current_bidding_price()

        # call the payment system to freeze amount from the user,
        # if the user has the money available
        bid_received = Payment.receive_bid_from_user(
            user_id=user_id,
            amount=amount,
            auction_id=self.get_auction_id(),
            highest_bid=self.get_highest_bid(),
        )

        # on success receive the bid and update database
        if bid_received:

            print("bid received")
        else:
            # otherwise let the user know that they were not able to place their bid
            print(
                "BID NOT RECEIVED FROM THE USER."
                + "WE WERE NOT ABLE TO HOLD THE BIDDING AMOUNT FROM YOUR ACCOUNT"
            )

    def able_to_place_bid(self, user: User):
        """check whether a user is able to place bid on the auction"""
        # user is a buyer
        # user is not the author of the auction
        # the auction is still in progress
        if (
            not self.has_timed_out()
            or self.is_own_auction(user)
        ):
            return False
        return True

    def is_own_auction(self, cur_user: User):
        """check if the auction belongs to the inputted user"""
        if str(cur_user.get_id()) == str(self.get_seller_id()):
            return True
        return False

    def has_timed_out(self):
        """return if the auction is not on sale anymore"""
        timed_out = self.get_end_time() <= datetime.datetime.now()
        if timed_out:
            self.state = "ended"
        return timed_out

    def payment_has_been_claimed(self):
        """check wherther the payment has been sent to the seller"""
        return False

    def pay_seller(self):
        """pay the seller for their auction"""
        Payment.pay_seller(self)

    def complete_auction(self):
        self.set_state(Shipped())
        Shipment.ship_art(self.auction_id)
        result = Authentication.authenticate_art(self)
        if result == "authenticated":
            self.set_state(Authenticated())
        elif result == "rejected":
            self.set_state(Rejected())

    def has_user_won_auction(self, cur_user: User):
        """check whether the user has won the auction"""
        if self.has_timed_out():
            winning_bid = self.get_highest_bid()
            if winning_bid is not None:
                if str(cur_user.get_id()) == str(winning_bid.get_user_id()):
                    return True
        return False

    def iterate_over_bids(self):
        """ method to print id's of all the bids that have been placed on the auction """
        collection = self.get_bids()
        iterator = BidIterator(collection=collection, reverse=False)
        while iterator.has_next():
            print(iterator.__next__())
        iterator.__next__()
