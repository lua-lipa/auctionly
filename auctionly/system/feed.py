from auctionly.art.art import Art
from auctionly.users.user import User
from auctionly.auction.auction import Auction

class Feed: 
    def __init__(self, art_prefs, user_id):
        self.all_art = Art.query.all()
        self.art_for_feed = []
        self.user_id = user_id
        for art in self.all_art:
            if art.get_art_category() in art_prefs:
                if art.get_owner() != self.user_id:
                    self.art_for_feed.append(art)
    
    def get_users_feed(self):
        return self.art_for_feed
    
    def get_feed(self):
        for art in self.all_art:
            if art.get_owner() != self.user_id:
                self.art_for_feed.append(art)
        return self.art_for_feed
    
    def get_user_name(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        name = user.get_full_name()
        return name
    
    def get_art_auction_id(self, art_id):
        auction = Auction.query.filter_by(art_id=art_id).first()
        auction_id = auction.get_auction_id()
        return auction_id

