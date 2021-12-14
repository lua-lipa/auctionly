""" Shipment class to handle shipping of auctionable items """
from random import random


class Shipment():
    """ shipping class handles shipping auctionable items """
    invoice_number = 0

    def __init__(self):
        """ constructor """
        self.invoice_number = 0

    def ship_art(self, auction_id):
        """ changing the state of shipment, generating random invoice number """
        self.invoice_number = auction_id + random.randint(1, 100000)
        print("The shipment service has received a request for shipment, please refer to your invoice number at" + str(self.invoice_number))

    def ship_art_to_buyer(self):
        """ ship art to buyer """
        print("shipped to buyer")

    def ship_art_to_seller(self):
        """ ship art to seller """
        print("shipped to seller")

    def get_invoice_number(self):
        """ return invoice number """
        return self.invoice_number

    def set_invoice_number(self, invoice_number):
        """ set invoice number """
        self.invoice_number = invoice_number
