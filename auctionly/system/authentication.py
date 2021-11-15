import random


def authenticate_art(art_id):
    """mocking the authentication process, 1 out of a 100 pieces will come back as fake """
    probability = random.randInt(1000)

    if (probability <= 900):
        print("Art successfully authenticated")
        # update the state of the art
    else:
        print("Art was not authenticated. Came back as fake.")
        # update the state of the art
        # system will continue to block the seller and request a penalty
