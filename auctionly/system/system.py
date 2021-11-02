"""module for system class"""
class System:
    """System class contains information on users of the system to be used by other classes"""
    sellers = []
    buyers = []

    def add_a_seller(self, seller):
        """called when a new seller account is created"""
        self.sellers.append(seller)

    def add_a_buyer(self, buyer):
        """called when a new buyer account is created"""
        self.buyers.append(buyer)
