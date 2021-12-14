""" Unit testing the payment system """
import unittest
from auctionly.system.payment import Payment


class TestPayment(unittest.TestCase):
    """ class to unit test the payment system """
    def test_unfreezing(self):
        """ unfreezing the payment and checking that it matches with the expected amount """
        payment = Payment(user_id=1, auction_id=1,
                          time=0, amount=100, bid_id=1)
        payment.unfreeze_payment()
        amount_after_unfreeze = payment.get_amount()
        expected_amount_after_unfreeze = 0
        self.assertEqual(expected_amount_after_unfreeze, amount_after_unfreeze)
