# from ..art import Art

from random import random


class Shipment():

    def ship_art(art_id):
        invoice_number = art_id + random.randint(1, 100000)
        print("The shipment service has received a request for shipment, please refer to your invoice number at" + str(invoice_number))
