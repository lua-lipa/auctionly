from users import User
from users import Buyer
import unittest
from unittest.mock import MagicMock
import logging


class TestUser(unittest.TestCase):

    def test_user_init(self):
        user_id = 1
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        user = User(user_id, name, last_name, email, password)

        logger = logging.getLogger()

        self.assertEquals(user_id, user.get_user_id())
        self.assertEquals(name, user.get_user_name())
        self.assertEquals(last_name, user.get_last_name())
        self.assertEquals(email, user.get_email)
        self.assertEquals(password, user.get_user_password())


class TestBuyer(unittest.TestCase):

    def test_buyer_init(self):
        user_id = 1
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        buyer = User(user_id, name, last_name, email, password)

        logger = logging.getLogger()

        self.assertEquals(user_id, buyer.get_user_id())
        self.assertEquals(name, buyer.get_user_name())
        self.assertEquals(last_name, buyer.get_last_name())
        self.assertEquals(email, buyer.get_email)
        self.assertEquals(password, buyer.get_user_password())

    def test_buyer_art_prefs(self):
        user_id = 1
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"

        buyer = Buyer(user_id, name, last_name, email, password)
        input_art_prefs = ["Modern", "Contemporary"]
        buyer.set_art_prefs(input_art_prefs)

        self.assertEquals(buyer.get_art_prefs(), input_art_prefs)

    def test_buyer_feed(self):
        user_id = 1
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"

        buyer = Buyer(user_id, name, last_name, email, password)
        input_buyer_feed = ["123", "456"]
        buyer.set_art_displayed_on_feed(input_buyer_feed)
        self.assertEquals(buyer.get_art_displayed_on_feed(), input_buyer_feed)

    def test_buyer_purchase_history(self):
        user_id = 1
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"

        buyer = Buyer(user_id, name, last_name, email, password)
        input_purchase_history = ["123", "456"]
        buyer.set_purchase_history(input_purchase_history)

        self.assertEquals(buyer.get_purchase_history(), input_purchase_history)
