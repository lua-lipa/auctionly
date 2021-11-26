from .. import db
from .ranked_user import Ranked_User
from .sale import Sale
import datetime
from auctionly.users.user import User
from auctionly.users.buyer import Buyer
from auctionly.users.seller import Seller

class Rank():

    def __init__(self):
        table_populated = Ranked_User.query.all()
        if table_populated:
            self.first_place_seller = Ranked_User.query.filter((Ranked_User.rank==1) & (Ranked_User.user_type=='Seller')).first()
            self.second_place_seller = Ranked_User.query.filter((Ranked_User.rank==2) & (Ranked_User.user_type=='Seller')).first()
            self.third_place_seller = Ranked_User.query.filter((Ranked_User.rank==3) & (Ranked_User.user_type=='Seller')).first()
            self.first_place_buyer = Ranked_User.query.filter((Ranked_User.rank==1) & (Ranked_User.user_type=='Buyer')).first()
            self.second_place_buyer = Ranked_User.query.filter((Ranked_User.rank==2) & (Ranked_User.user_type=='Buyer')).first()
            self.third_place_buyer = Ranked_User.query.filter((Ranked_User.rank==3) & (Ranked_User.user_type=='Buyer')).first()
            self.date = self.first_place_buyer.get_date_ranked()
            rank = ((datetime.datetime.now() - datetime.timedelta(days=7)) == self.date)
            if rank:
                self.rank_users()
        else:
            self.rank_users()

    def rank_users(self):
        users = User.query.all()
        count = 3
        sellers = []
        top_ranked_sellers = []
        buyers = []
        top_ranked_buyers = []
        
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
            if(sales > sales_1):
                top_ranked_sellers[2] = top_ranked_sellers[1]
                top_ranked_sellers[1] = top_ranked_sellers[0]
                top_ranked_sellers[0] = seller
            elif(sales > sales_2 and sales < sales_1):
                top_ranked_sellers[2] = top_ranked_sellers[1]
                top_ranked_sellers[1] = seller
            elif(sales > sales_3 and sales < sales_2):
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
            if(buys > buys_1):
                top_ranked_buyers[2] = top_ranked_buyers[1]
                top_ranked_buyers[1] = top_ranked_buyers[0]
                top_ranked_buyers[0] = buyer
            elif(buys > buys_2 and buys < buys_1):
                top_ranked_buyers[2] = top_ranked_buyers[1]
                top_ranked_buyers[1] = buyer
            elif(buys > buys_3 and buys < buys_2):
                top_ranked_buyers[2] = buyer
        
        Ranked_User.query.delete()
        
        ranked_seller_1 = Ranked_User(top_ranked_sellers[0].get_user_id(), 1, "Seller")
        ranked_seller_2 = Ranked_User(top_ranked_sellers[1].get_user_id(), 2, "Seller")
        ranked_seller_3 = Ranked_User(top_ranked_sellers[2].get_user_id(), 3, "Seller")
        db.session.add(ranked_seller_1)
        db.session.add(ranked_seller_2)
        db.session.add(ranked_seller_3)

        ranked_buyer_1 = Ranked_User(top_ranked_buyers[0].get_user_id(), 1, "Buyer")
        ranked_buyer_2 = Ranked_User(top_ranked_buyers[1].get_user_id(), 2, "Buyer")
        ranked_buyer_3 = Ranked_User(top_ranked_buyers[2].get_user_id(), 3, "Buyer")
        db.session.add(ranked_buyer_1)
        db.session.add(ranked_buyer_2)
        db.session.add(ranked_buyer_3)
        
        db.session.commit()
        
    def get_seller_rank(self, user_id):
        rank = "No rank"
        if self.first_place_seller.get_user_id() == user_id:
            rank = "First place"
        elif self.second_place_seller.get_user_id() == user_id:
            rank = "Second place"
        elif self.third_place_seller.get_user_id() == user_id:
            rank = "Third place"
        
        return rank
    
    def get_buyer_rank(self, user_id):
        rank = "No rank"
        if self.first_place_buyer.get_user_id() == user_id:
            rank = "First place"
        elif self.second_place_buyer.get_user_id() == user_id:
            rank = "Second place"
        elif self.third_place_buyer.get_user_id() == user_id:
            rank = "Third place"
        
        return rank
            
