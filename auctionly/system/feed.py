import sys
from system import System

class Feed:
    art_for_feed = []
    def get_users_feed(self, art_prefs):
        for art in System.art:
            if art.get_art_category in art_prefs:
                self.art_for_feed.append(art)

