from .user import User
from auctionly.system.shipment import Shipment


class Seller(User):
    def __init__(self, user_id, name, last_name, email, password):
        super().__init__(user_id, name, last_name, email, password)
        self.art_types = []
        self.art_for_exhibition = []
        self.art_for_auction = []
        self.art_sold = []

    def get_art_types(self):
        return self.art_types

    def set_art_types(self, art_types):
        self.art_types = art_types

    def add_art_type(self, art_type):
        self.art_types.append(art_type)

    def get_art_for_exhibition(self):
        return self.art_for_exhibition

    def set_art_types(self, art_for_exhibition):
        self.art_for_exhibition = art_for_exhibition

    # As a seller I want to be able to upload my art so that I can later put it up for exhibition
    def add_for_exhibition(self, art_for_exhibition):
        self.art_for_exhibition.append(art_for_exhibition)

    def get_art_for_auction(self):
        return self.art_for_auction

    def set_art_types(self, art_for_auction):
        self.art_for_auction = art_for_auction

    # As a seller I want to be able to set the art category my art relates to so that it reaches the correct  buyers.
    def add_art_type(self, art_type):
        self.art_types.append(art_type)

    #  As a seller I want to be able to upload my art so that I can later put it up for auction
    # As a seller I want to be able to start an auction for my art so that buyers can bid on it.
    def add_for_exhibition(self, art_for_auction):
        self.art_for_auction.append(art_for_auction)

    def get_art_sold(self):
        return self.art_sold

    def add_art_sold(self, art_sold):
        self.art_sold.append(art_sold)

    def get_money_earned(self):
        # this calls the treasury system
        # money_earned = treasury.lookup(user_id)
        pass

    def add_money_earned(self):
        pass

    # As a seller I want to be able to receive incentives for my loyalty so that I have added benefits.
    def update_loyalty_points(self):
        # calls the ranking system
        pass

    # As a seller I want to be able to ship the art safely so that it doesn’t get damaged.
    def ship_art(self, art_id):
        # calls the art shipment system
        shipment = Shipment()
        shipment.ship_art(art_id)

    # As a seller I want to be able to update my ongoing auctions properties so that I can help it do better to increase my chances of a higher bid.
    def update_art_auction_property(self):
        # calls the Auction class to update properties
        pass

    # As a seller I want to be able to complete a sale of my art so I can earn money.
