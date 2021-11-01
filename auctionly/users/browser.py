import user


class browser(user):
    def __init__(self, user_id, name, last_name, email, password):
        super().__init__(self, user_id, name, last_name, email, password)
        self.art_displayed_on_feed = []

    # As a browser I want to be able to view the art that is available on the website so that I don't have to create an account unless I'm interested.
    def display_art_on_home_page(self):
        return

    # As a browser I want to be able to create an account if I want to so that I can buy/sell art.
    def create_account(self):
        return
