"""module containing rank class"""
# pylint: disable=E0401
# pylint: disable=E0402
import datetime
from auctionly.users.user import User
from .. import db
from .ranked_user import RankedUser
from .sale import Sale

class Rank():
    """Rank class implemented to handle the ranking of users"""
    def __init__(self):
        """created a rank object to be used in other classes"""
        table_populated = RankedUser.query.all() # checking if there is data in the tables before trying to extract it
        if table_populated:
            # getting the ranked sellers
            self.first_place_seller = RankedUser.query.filter((RankedUser.rank==1) & (RankedUser.user_type=='Seller')).first()
            self.second_place_seller = RankedUser.query.filter((RankedUser.rank==2) & (RankedUser.user_type=='Seller')).first()
            self.third_place_seller = RankedUser.query.filter((RankedUser.rank==3) & (RankedUser.user_type=='Seller')).first()

            # getting the ranked buyers
            self.first_place_buyer = RankedUser.query.filter((RankedUser.rank==1) & (RankedUser.user_type=='Buyer')).first()
            self.second_place_buyer = RankedUser.query.filter((RankedUser.rank==2) & (RankedUser.user_type=='Buyer')).first()
            self.third_place_buyer = RankedUser.query.filter((RankedUser.rank==3) & (RankedUser.user_type=='Buyer')).first()

            # getting the date of the last ranking
            self.date = self.first_place_buyer.get_date_ranked()

            # checking if its been a week and time for a new ranking
            rank = ((datetime.datetime.now() - datetime.timedelta(days=7)) == self.date)
            if rank:
                self.rank_users()
        else:
            self.rank_users()

    # pylint: disable=R0914
    # pylint: disable=R0912
    # pylint: disable=R0915
    def rank_users(self):
        """ranks buyers and sellers according to their sale and purchase history"""

        # getting all the users so we can find the top ones
        users = User.query.all()

        # we're only ranking 3 sellers and 3 buyers
        count = 3

        # initialising sellers arrays
        sellers = []
        top_ranked_sellers = []

        # initialising buyers arrays
        buyers = []
        top_ranked_buyers = []

        # looping through users and seperating them according to their type
        for user in users:
            if user.get_user_type() == 'Seller':
                sellers.append(user)
            elif user.get_user_type() == 'Buyer':
                buyers.append(user)

        #add first three sellers initially
        for seller in sellers:
            if(len(top_ranked_sellers)) >= count:
                break
            top_ranked_sellers.append(seller)

        #loop through the rest of the sellers and rank them
        for seller in sellers:
            sales = len(Sale.query.filter_by(sold_by=seller.get_user_id()).all()) # sales of current seller in loop
            sales_1 = len(Sale.query.filter_by(sold_by=top_ranked_sellers[0].get_user_id()).all()) # sales of seller currently in first place
            sales_2 = len(Sale.query.filter_by(sold_by=top_ranked_sellers[1].get_user_id()).all()) # sales of seller currently in second place
            sales_3 = len(Sale.query.filter_by(sold_by=top_ranked_sellers[2].get_user_id()).all()) # sales of seller currently in third place
            if sales > sales_1:
                top_ranked_sellers[2] = top_ranked_sellers[1]
                top_ranked_sellers[1] = top_ranked_sellers[0]
                top_ranked_sellers[0] = seller
            elif sales_1 > sales > sales_2:
                top_ranked_sellers[2] = top_ranked_sellers[1]
                top_ranked_sellers[1] = seller
            elif sales_2 > sales > sales_3:
                top_ranked_sellers[2] = seller

        #add first three buyers initially
        for buyer in buyers:
            if(len(top_ranked_buyers)) >= count:
                break
            top_ranked_buyers.append(buyer)

        #loop through the rest of the buyers and rank them
        for buyer in buyers:
            buys = len(Sale.query.filter_by(bought_by=buyer.get_user_id()).all()) # buys of current buyer in loop
            buys_1 = len(Sale.query.filter_by(bought_by=top_ranked_buyers[0].get_user_id()).all()) # buys of buyer currently in first place
            buys_2 = len(Sale.query.filter_by(bought_by=top_ranked_buyers[1].get_user_id()).all()) # buys of buyer currently in second place
            buys_3 = len(Sale.query.filter_by(bought_by=top_ranked_buyers[2].get_user_id()).all()) # buys of buyer currently in third place
            if buys > buys_1:
                top_ranked_buyers[2] = top_ranked_buyers[1]
                top_ranked_buyers[1] = top_ranked_buyers[0]
                top_ranked_buyers[0] = buyer
            elif buys_1 > buys > buys_2:
                top_ranked_buyers[2] = top_ranked_buyers[1]
                top_ranked_buyers[1] = buyer
            elif buys_2 > buys > buys_3:
                top_ranked_buyers[2] = buyer

        # empty the table in preparation for new ranking
        RankedUser.query.delete()

        # add in the newly ranked sellers
        self.first_place_seller = RankedUser(top_ranked_sellers[0].get_user_id(), 1, "Seller")
        self.second_place_seller = RankedUser(top_ranked_sellers[1].get_user_id(), 2, "Seller")
        self.third_place_seller = RankedUser(top_ranked_sellers[2].get_user_id(), 3, "Seller")
        db.session.add(self.first_place_seller)
        db.session.add(self.second_place_seller)
        db.session.add(self.third_place_seller)

        # add in the newly ranked buyers
        self.first_place_buyer = RankedUser(top_ranked_buyers[0].get_user_id(), 1, "Buyer")
        self.second_place_buyer = RankedUser(top_ranked_buyers[1].get_user_id(), 2, "Buyer")
        self.third_place_buyer = RankedUser(top_ranked_buyers[2].get_user_id(), 3, "Buyer")
        db.session.add(self.first_place_buyer)
        db.session.add(self.second_place_buyer)
        db.session.add(self.third_place_buyer)

        db.session.commit()

    def get_seller_rank(self, user_id):
        """returns the ranking of a specified seller"""
        rank = "No rank"
        if self.first_place_seller.get_user_id() == user_id:
            rank = "First place"
        elif self.second_place_seller.get_user_id() == user_id:
            rank = "Second place"
        elif self.third_place_seller.get_user_id() == user_id:
            rank = "Third place"

        return rank

    def get_buyer_rank(self, user_id):
        """returns the ranking of a specified buyer"""
        rank = "No rank"
        if self.first_place_buyer.get_user_id() == user_id:
            rank = "First place"
        elif self.second_place_buyer.get_user_id() == user_id:
            rank = "Second place"
        elif self.third_place_buyer.get_user_id() == user_id:
            rank = "Third place"

        return rank
