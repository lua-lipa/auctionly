from abc import ABC, abstractmethod


class IAuctionState(ABC):
    @staticmethod
    @abstractmethod
    def __str__():
        pass

class Started(IAuctionState):
    def __str__(self):
        return "Started"

class Ended(IAuctionState):
    def __str__(self):
        return "Ended"

class Shipped(IAuctionState):
    def __str__(self):
        return "Shipped"

class Authenticated(IAuctionState):
    def __str__(self):
        return "Authenticated"

class Rejected(IAuctionState):
    def __str__(self):
        return "Rejected"

class ShippedToBuyer(IAuctionState):
    def __str__(self):
        return "ShippedToBuyer"

class ShippedToSeller(IAuctionState):
    def __str__(self):
        return "ShippedToSeller"
