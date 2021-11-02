import sys
from system import System

class Rank(System):
    top_ranked_buyers = [] #top 3
    top_ranked_sellers = [] #top 3

    def rank_buyers(self):
        count = 3

        #add first three buyers initially
        for buyer in System.buyers:
            if(len(self.top_ranked_buyers)) >= count:
                break
            self.top_ranked_buyers.append(buyer)
        
        for buyer in System.buyers:
            if(buyer.get_number_of_purchases() > self.top_ranked_buyers[0].get_number_of_purchases()):
                self.top_ranked_buyers[2] = self.top_ranked_buyers[1]
                self.top_ranked_buyers[1] = self.top_ranked_buyers[0]
                self.top_ranked_buyers[0] = buyer
            elif (buyer.get_number_of_purchases() > self.top_ranked_buyers[1].get_number_of_purchases()):
                self.top_ranked_buyers[2] = self.top_ranked_buyers[1]
                self.top_ranked_buyers[1] = buyer
            elif (buyer.get_number_of_purchases() > self.top_ranked_buyers[2].get_number_of_purchases()):
                self.top_ranked_buyers[2] = buyer
    
    def rank_sellers(self):
        count = 3

        #add first three sellers initially
        for seller in System.sellers:
            if(len(self.top_ranked_sellers)) >= count:
                break
            self.top_ranked_sellers.append(seller)
        
        for seller in System.sellers:
            if(seller.get_number_of_sales() > self.top_ranked_sellers[0].get_number_of_sales()):
                self.top_ranked_sellers[2] = self.top_ranked_sellers[1]
                self.top_ranked_sellers[1] = self.top_ranked_sellers[0]
                self.top_ranked_sellers[0] = seller
            elif (seller.get_number_of_sales() > self.top_ranked_sellers[1].get_number_of_sales()):
                self.top_ranked_sellers[2] = self.top_ranked_sellers[1]
                self.top_ranked_sellers[1] = seller
            elif (seller.get_number_of_sales() > self.top_ranked_sellers[2].get_number_of_sales()):
                self.top_ranked_sellers[2] = seller
