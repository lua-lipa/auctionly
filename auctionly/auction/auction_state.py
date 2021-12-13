from abc import ABC, abstractmethod


class IAuctionState(ABC):
    @staticmethod
    @abstractmethod
    def __str__():
        "Set the default method"

class Started(IAuctionState):
    def __str__():
        "Started"

class Ended(IAuctionState):
    def __str__():
        "Ended"

class Shipped(IAuctionState):
    def __str__():
        "Shipped"

class Authenticated(IAuctionState):
    def __str__():
        "Authenticated"

class Rejected(IAuctionState):
    def __str__():
        "Rejected"
