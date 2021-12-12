""" Seller is a subclass of User"""
from auctionly.system.shipment import Shipment
from auctionly.users.user import User


class Seller(User):
    """ Creating the seller object and returning information for it"""

    def __init__(self, name, last_name, email, password):
        super().__init__(name, last_name, email, password)
        self.art_types = []
        self.art_for_exhibition = []
        self.art_for_auction = []
        self.art_sold = []

    def get_art_types(self):
        """ return art types: i.e. what kind of art the user is selling """
        return self.art_types

    def set_art_types(self, art_types):
        """ set art types: i.e. what kind of art the user is selling """
        self.art_types = art_types

    def add_art_type(self, art_type):
        """ add new art type: i.e. what kind of art the user is selling """
        self.art_types.append(art_type)

    def get_art_for_exhibition(self):
        """ return which art items the seller has up for exhibition """
        return self.art_for_exhibition

    def set_art_for_exhibition(self, art_for_exhibition):
        """ set art items the seller has up for exhibition """
        self.art_for_exhibition = art_for_exhibition

    # As a seller I want to be able to upload my art so that I can later put it up for exhibition
    def add_for_exhibition(self, art_for_exhibition):
        """ add new art for exhibition """
        self.art_for_exhibition.append(art_for_exhibition)

    def get_art_for_auction(self):
        """ return which art items the seller has up for auction """
        return self.art_for_auction

    def set_art_for_auction(self, art_for_auction):
        """ set art for auction placed by the seller """
        self.art_for_auction = art_for_auction

    #  As a seller I want to be able to upload my art so that I can later put it up for auction
    # As a seller I want to be able to start an auction for my art so that buyers can bid on it.
    def get_art_sold(self):
        """ return art items the user has sold """
        return self.art_sold

    def add_art_sold(self, art_sold):
        """ add art items the user has sold """
        self.art_sold.append(art_sold)

    def get_money_earned(self):
        """ return how much money the user has made: TO-DO """
        return 0

    def add_money_earned(self):
        """ add new income for the user: TO-DO """
        return 0

    # As a seller I want to be able to ship the art safely so that it doesn’t get damaged.
    def ship_art(self, art_id):
        """ calls the shipment system to ship art placed by the seller """
        # calls the art shipment system
        shipment = Shipment()
        shipment.ship_art(art_id)
