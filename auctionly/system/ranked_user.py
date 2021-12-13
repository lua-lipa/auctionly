"""module containing Ranked User class"""
# pylint: disable=E0402
from datetime import datetime
from .. import db

class RankedUser(db.Model):
    """Ranked user class used to make a table in the database to store the users that are ranked"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    rank = db.Column(db.Integer)
    date = db.Column(db.Date)
    user_type = db.Column(db.String(6))

    def __init__(self, user_id, rank, user_type):
        """used to make rows in the table"""
        self.user_id = user_id
        self.rank = rank
        self.date = datetime.today()
        self.user_type = user_type

    def get_user_id(self):
        """returns the id of the user that has been ranked"""
        return self.user_id

    def get_date_ranked(self):
        """returns the date they were last ranked"""
        return self.date

    def get_rank(self):
        """returns the ranking they recieved 1, 2, 3"""
        return self.rank

    def get_user_type(self):
        """returns the type of user it is"""
        return self.user_type
