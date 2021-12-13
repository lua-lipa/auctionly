import random

class Authentication():

    def authenticate_art():
        """mocking the authentication process, 1 out of a 100 pieces will come back as fake """
        probability = random.randInt(1000)

        if probability <= 900:
           return "authenticated"
            # update the state of the art
        else:
            return "rejected"
            
            # update the state of the art
            # system will continue to block the seller and request a penalty
