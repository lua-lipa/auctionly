""" DutchAuction is a subclass of the Auction class """
from datetime import datetime
from .auction import Auction


class DutchAuction(Auction):
    """ subclass of the auction class with specific variables"""
    start_time = datetime.now()
    bid_increment = 10

    def set_bid_increment(self):
        """ setting the bid increment """
        self.bid_increment = 10
        return super().set_bid_increment()

    def get_bid_increment(self):
        """ returning the bid increment """
        return self.bid_increment

    def get_start_time(self):
        """ returning the auction start time """
        return self.start_time

    def set_start_time(self):
        """ setting the auction start time """
        self.start_time = datetime.now()
