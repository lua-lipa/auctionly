import user


class browser(user):
    def __init__(self, user_id, name, last_name, email, password):
        super().__init__(self, user_id, name, last_name, email, password)
        self.art_displayed_on_feed = []

    def get_art_displayed_on_feed(self):
        return self.art_displayed_on_feed

    def set_art_displayed_on_feed(self, art_displayed_on_feed):
        self.art_displayed_on_feed = art_displayed_on_feed

    def add_art_displayed_on_feed(self, art):
        self.art_displayed_on_feed.append(art)
