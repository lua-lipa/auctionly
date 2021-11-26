from .. import db
from datetime import datetime

class Ranked_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    rank = db.Column(db.Integer)
    date = db.Column(db.Date)
    user_type = db.Column(db.String(6))

    def __init__(self, user_id, rank, user_type):
        self.user_id = user_id
        self.rank = rank
        self.date = datetime.today()
        self.user_type = user_type

    def get_user_id(self):
        return self.user_id

    def get_date_ranked(self):
        return self.date
    
    def get_rank(self):
        return self.rank
    
    def get_user_type(self):
        return self.user_type