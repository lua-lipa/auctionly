from auctionly.art.art import Art

class Feed: 
    def __init__(self, art_prefs):
        self.all_art = Art.query.all()
        self.art_for_feed = []
        for art in self.all_art:
            if art.get_art_category() in art_prefs:
                self.art_for_feed.append(art)
    
    def get_users_feed(self):
        return self.art_for_feed
    
    def get_feed(self):
        return self.all_art