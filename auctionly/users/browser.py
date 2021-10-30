import user

# As a browser I want to be able to view the art that is available on the website so that I don't have to create an account unless I'm interested.
#As a browser I want to be able to create an account if I want to so that I can buy/sell art.#


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

    # def create_account(self, user)

    # create account
    # check if user is logged in
    # let them apply to purchase an account
