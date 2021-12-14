""" System for authenticating auction """
import random

from auctionly.system.payment import Payment


class Authentication():
    """ class for authenticating art """
    probability_fraction = 900

    def authenticate_art(self):
        """mocking the authentication process, 1 out of a 100 pieces will come back as fake """
        probability = random.randInt(1000)

        if probability <= self.probability_fraction:
            return "authenticated"
            # update the state of the art
        return "rejected"
        # update the state of the art
        # system will continue to block the seller and request a penalty

    def set_probability(self, probability):
        """ setting the probability to change the mocking process """
        self.probability_fraction = probability
