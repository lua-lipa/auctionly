""" User class implemented to provide parent class methods to its children """


class User:

    def __init__(self, user_id, name, last_name, email, password):
        self.user_id = user_id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        # to-do: implement hashing function for password
        pass
