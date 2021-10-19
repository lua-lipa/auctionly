import user


class seller(user):
    def __init__(self, user_id, name, last_name, email, password):
        super().__init__(self, user_id, name, last_name, email, password)
        self.art_types = []
        self.art_for_exhibition = []
        self.art_for_auction = []
        self.art_sold = []
        self.art_displayed_on_feed = []

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

    def add_for_exhibition(self, art_for_exhibition):
        self.art_for_exhibition.append(art_for_exhibition)

    def get_art_for_auction(self):
        return self.art_for_auction

    def set_art_types(self, art_for_auction):
        self.art_for_auction = art_for_auction

    def add_for_exhibition(self, art_for_auction):
        self.art_for_auction.append(art_for_auction)

    def get_art_sold(self):
        return self.art_sold

    def add_art_sold(self, art_sold):
        self.art_sold.append(art_sold)
