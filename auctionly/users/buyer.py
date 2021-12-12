""" Buyer: subclass of User """
from .user import User


class Buyer(User):
    """ handles the creation and fetching of a Buyer object"""

    def __init__(self, name, last_name, email, password):
        super().__init__(name, last_name, email, password)
        self.art_prefs = []
        self.purchase_history = []
        self.bidding_history = []

    def get_art_prefs(self):
        """ return buyer art preferences """
        return self.art_prefs

    def set_art_prefs(self, art_prefs):
        """ return buyer art preferences """
        self.art_prefs = art_prefs

    def add_art_pref(self, art_pref):
        """ add new art preferences """
        self.art_prefs.append(art_pref)

    def get_purchase_history(self):
        """ get purchase history for the buyer """
        return self.purchase_history

    def set_purchase_history(self, purchase_history):
        """ set purchase history for the buyer """
        self.purchase_history = purchase_history

    def add_purchase_history(self, art):
        """ add new purchase for the buyer """
        self.purchase_history.append(art)

    def get_bidding_history(self):
        """ get bidding history for buyer """
        return self.bidding_history

    def set_bidding_history(self, bidding_history):
        """ set bidding history for buyer """
        self.bidding_history = bidding_history

    def add_bidding_history(self, bid):
        """ add new bidding history to the current history  """
        self.bidding_history.append(bid)
