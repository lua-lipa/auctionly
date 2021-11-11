from .users import buyer, seller

email = "test@test.com"
first_name = "john"
last_name = "smith"
password = "pass"
accountType = "Buyer"

def test():
    new_user = buyer('0', first_name, last_name, email, password)
    print(new_user)