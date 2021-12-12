"""module containing feed class"""
from auctionly.art.art import Art
from auctionly.users.user import User
from auctionly.auction.auction import Auction

class Feed: 
    """Feed class implemented to create feeds for users"""
    def __init__(self, user_id):
        """creates a feed object"""
        self.all_art = Art.query.all()
        self.art_for_feed = []
        self.user_id = user_id
    
    def get_users_feed(self, art_prefs):
        """returns feed thats catered to the users preferences"""
        for art in self.all_art:
            if art.get_art_category() in art_prefs:
                if art.get_owner() != self.user_id:
                    self.art_for_feed.append(art)
        return self.art_for_feed
    
    def get_feed(self):
        """returns a feed of all art that isn't the users"""
        for art in self.all_art:
            if art.get_owner() != self.user_id:
                self.art_for_feed.append(art)
        return self.art_for_feed
    
    def get_user_name(self, user_id):
        """returns a users name"""
        user = User.query.filter_by(id=user_id).first()
        name = user.get_full_name()
        return name
    
    def get_art_auction_id(self, art_id):
        """returns the auction id of a particular art piece"""
        auction = Auction.query.filter_by(art_id=art_id).first()
        auction_id = auction.get_auction_id()
        return auction_id

