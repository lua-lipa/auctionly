from auctionly import db
import datetime
from auctionly.bid.bid import Bid
from auctionly.art.art import Art
from auctionly.users.user import User
from auctionly.system.payment import Payment


class Auction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    end_time = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    art_id = db.Column(db.Integer, db.ForeignKey("art.id"))
    description = db.Column(db.String(150))
    starter_price = db.Column(db.String(150))
    bid_increment = db.Column(db.String(150))
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, end_time, seller_id, art_id,
                 description, starter_price, bid_increment):
        # auction_description, starter_price, bid_increment, auction_type, sold, buyer_id, bids, payment):
        self.end_time = end_time
        self.seller_id = seller_id
        self.art_id = art_id
        self.auction_description = description
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
        return self.id

    def get_art_id(self):
        return self.art_id

    def get_auction_description(self):
        return self.description

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

    def get_payment(self):
        return self.payment

    def set_auction_description(self, description):
        self.description = description

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

    def get_time_since_start(self):
        """ displays how much time has passed since the beginning of the auction """
        now = datetime.datetime.now()
        return (now - self.get_upload_time())

    def get_time_left(self):
        """ returns how much time is left before the auction ends """
        """ by default it is set to last 3 days since the start of the auction """
        time_out = self.get_upload_time() + datetime.timedelta(days=3)
        now = datetime.datetime.now()
        return (time_out - now)

    def get_bids(self):
        return Bid.query.filter_by(auction_id=self.get_auction_id()).all()

    def get_highest_bid(self):
        """ returns the BID object of the highest bid """
        if (self.get_number_of_bids() == 0):
            return None

        bids = self.get_bids()
        highest_bid_amount = int(self.get_starter_price())
        highest_bid = None
        for bid in bids:
            if (bid.get_amount() >= highest_bid_amount):
                highest_bid_amount = bid.get_amount()
                highest_bid = bid

        return highest_bid

    def get_latest_bid(self):
        """ returns the HIGHEST BIDDING AMOUNT placed on the item """
        highest_bid = self.get_highest_bid()
        if (highest_bid == None):
            return 0
        else:
            return highest_bid.get_amount()

    def get_current_bidding_price(self):
        if len(self.get_bids()) == 0:
            return self.get_starter_price()
        else:
            latest_bid = self.get_latest_bid()
            return int(latest_bid) + int(self.get_bid_increment())

    def get_number_of_bids(self):
        return len(self.get_bids())

    def get_title(self):
        art = Art.query.filter_by(id=self.get_art_id()).one()
        return art.get_name()

    def place_bid(self, user_id):

        # get the amount of the next bid to be placed
        amount = self.get_current_bidding_price()
        time = datetime.datetime.now()

        # call the payment system to freeze amount from the user, if the user has the money available
        bid_received = Payment.receive_bid_from_user(
            user_id=user_id, amount=amount, auction_id=self.get_auction_id(), highest_bid=self.get_highest_bid())

        # on success receive the bid and update database
        if (bid_received):

            print("bid received")
        else:
            # otherwise let the user know that they were not able to place their bid
            print(
                "BID NOT RECEIVED FROM THE USER. WE WERE NOT ABLE TO HOLD THE BIDDING AMOUNT FROM YOUR ACCOUNT")
