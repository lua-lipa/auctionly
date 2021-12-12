""" Class for unit testing the users package. """
import unittest
from auctionly.users.user import User
from auctionly.users.buyer import Buyer


class TestUser(unittest.TestCase):
    """ class for unit testing the user class"""

    def test_user_init(self):
        """ testing the User object constructor """
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        user = User(name, last_name, email, password)
        self.assertEqual(name, user.get_name())
        self.assertEqual(last_name, user.get_last_name())


class TestBuyer(unittest.TestCase):
    """ class for unit testing the buyer class """

    def test_buyer_init(self):
        """ testing the Buyer object constructor """
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        buyer = User(name, last_name, email, password)
        self.assertEqual(name, buyer.get_name())
        self.assertEqual(last_name, buyer.get_last_name())

    def test_buyer_art_prefs(self):
        """ testing the Buyer object art preference setting """
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"

        buyer = Buyer(name, last_name, email, password)
        input_art_prefs = ["Modern", "Contemporary"]
        buyer.set_art_prefs(input_art_prefs)
        self.assertEqual(buyer.get_art_prefs(), input_art_prefs)
