from auctionly.users.user import User
from auctionly.users.buyer import Buyer
import unittest
from unittest.mock import MagicMock
import logging
import pytest


class TestUser(unittest.TestCase):

    def test_user_init(self):
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        user = User(name, last_name, email, password)

        logger = logging.getLogger()

        self.assertEqual(name, user.get_name())
        self.assertEqual(last_name, user.get_last_name())
        # self.assertEqual(email, user.get_email)
        # self.assertEqual(password, user.get_password())


class TestBuyer(unittest.TestCase):

    def test_buyer_init(self):
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"
        buyer = User(name, last_name, email, password)

        logger = logging.getLogger()

        self.assertEqual(name, buyer.get_name())
        self.assertEqual(last_name, buyer.get_last_name())
        # self.assertEqual(email, buyer.get_email)
        # self.assertEqual(password, buyer.get_password())

    def test_buyer_art_prefs(self):
        name = "Nutsa"
        last_name = "CH"
        email = "test@gmail.com"
        password = "1234"

        buyer = Buyer(name, last_name, email, password)
        input_art_prefs = ["Modern", "Contemporary"]
        buyer.set_art_prefs(input_art_prefs)

        self.assertEqual(buyer.get_art_prefs(), input_art_prefs)
