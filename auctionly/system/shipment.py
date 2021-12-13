# from ..art import Art

from random import random
from auctionly.system.authentication import Authentication

class Shipment():

    def ship_art(auction_id):
        invoice_number = auction_id + random.randint(1, 100000)
        print("The shipment service has received a request for shipment, please refer to your invoice number at" + str(invoice_number))

        
