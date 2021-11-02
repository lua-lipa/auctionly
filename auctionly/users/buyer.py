from user import User


class Buyer(User):

    def __init__(self, user_id, name, last_name, email, password):
        super().__init__(user_id, name, last_name, email, password)
        self.art_prefs = []
        self.purchase_history = []
        self.bidding_history = []
        # self.BuyerRank = BuyerRank() TO-DO
        # self.BuyerProfile = BuyerProfile() TO-DO

    def get_art_prefs(self):
        return self.art_prefs

    def set_art_prefs(self, art_prefs):
        self.art_prefs = art_prefs

    def add_art_pref(self, art_pref):
        self.art_prefs.append(art_pref)

    def get_purchase_history(self):
        return self.purchase_history

    def set_purchase_history(self, purchase_history):
        self.purchase_history = purchase_history

    def add_purchase_history(self, art):
        self.purchase_history.append(art)

    def get_bidding_history(self):
        return self.bidding_history

    def set_bidding_history(self, bidding_history):
        self.bidding_history = bidding_history

    def add_bidding_history(self, bid):
        self.bidding_history.append(bid)

    def set_buyer_rank(buyer_rank):
        pass

    def get_buyer_rank():
        pass

    def place_bid():
        pass

    # As a buyer I want to have the art I buy displayed on my profile so that other users can see.
    def display_art_on_profile(self):
        return

    # As a buyer I want to be able to view a feed of the art so that I know what's available.
    def get_art_displayed_on_feed(self):
        return

    # Added - As a buyer I want to be able to filter the art that appears on my feed
    def set_art_displayed_on_feed(self):
        return

    # As a buyer I want to be able to bid on art in auctions so that I can buy them.
    def make_bid(self):
        return

    # As a buyer I want to be sure the art I'm receiving is authentic so that I don't get scammed.
    def is_art_authenticated(self):
        # calls authentication system where art has/hasnt been authenticated and return true if piece is authenticated
        return

    # As a buyer I want to have the art I buy shipped safely so that it doesn't get damaged.
    def set_shipping_method(self):
        return

    # As a buyer I want to be able to receive incentives for my loyalty so that I have added benefits.
    def display_loyalty_benefits(self):
        return
    
    def get_number_of_purchases(self):
        """will get number of purchases made by buyer, used by rank"""
        return len(self.purchase_history)
