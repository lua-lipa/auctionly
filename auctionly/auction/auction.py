# abstract auction class 

from abc import ABC, abstractmethod 
from datetime import datetime
from bid import bid 

class Auction(ABC): 
    @abstractmethod
    def set_start_time(self): 
        pass 

    @abstractmethod
    def get_start_time(self): 
        pass

    @abstractmethod
    def set_bid_increment(self): 
        pass

    @abstractmethod
    def get_bid_increment(self): 
        pass

    @abstractmethod
    def get_latest_bid(self): 
        pass

    @abstractmethod
    def add_bid(self, bid):
        pass
