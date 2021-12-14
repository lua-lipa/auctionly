from abc import ABC, abstractmethod


class IAuctionState(ABC):
    """ toggling the states of an auction """
    @staticmethod
    @abstractmethod
    def __str__():
        """ print status """
        return ""

class Started(IAuctionState):
    """ auction has started"""
    def __str__(self):
        """ print status """
        return "Started"

class Ended(IAuctionState):
    """ auction has ended """
    def __str__(self):
        """ print status """
        return "Ended"

class Shipped(IAuctionState):
    """ auction has shipped """
    def __str__(self):
        """ print status """
        return "Shipped"

class Authenticated(IAuctionState):
    """ auction has been authenticated """
    def __str__(self):
        """ print status """
        return "Authenticated"

class Rejected(IAuctionState):
    """ auction has been rejected """
    def __str__(self):
        """ print status """
        return "Rejected"

class ShippedToBuyer(IAuctionState):
    """ auction has been shipped to the buyer """
    def __str__(self):
        """ print status """
        return "ShippedToBuyer"

class ShippedToSeller(IAuctionState):
    """ auction has been shipped back to the seller """
    def __str__(self):
        """ print status """
        return "ShippedToSeller"