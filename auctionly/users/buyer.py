import user


class Buyer(user):

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
