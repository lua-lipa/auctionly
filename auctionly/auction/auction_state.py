class AuctionState(object):
    name = "state"

    def set_state(self, state):
        self.__class__ = state

    def __str__(self):
      return self.name

class Started(AuctionState):
    name = "started"

class Ended(AuctionState):
    name = "ended"

class Shipped(AuctionState):
    name ="shipped"

class Authenticated(AuctionState):
    name = "authenticated"

class Rejected(AuctionState):
    name = "rejected"