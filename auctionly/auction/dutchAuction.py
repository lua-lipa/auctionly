from datetime import datetime
from .auction import Auction


class DutchAuction(Auction):
    def set_bid_increment(self):
        self.bid_increment = 10
        return super().set_bid_increment()

    def get_bid_increment(self):
        return self.bid_increment

    def get_start_time(self):
        return self.start_time()

    def set_start_time(self):
        self.start_time = datetime.now()

    def get_latest_bid(self):
        pass

    def add_bid(self, bid):
        pass
