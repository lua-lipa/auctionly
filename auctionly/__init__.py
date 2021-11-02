from auctionly.auction.dutchAuction import DutchAuction
from users import seller
from users import buyer 
from art import art 
from auction import dutchAuction
def mock_auction_process(): 
    # set up seller and buyer
    seller_a = seller(user_id="1", 
                      name="Nutsa", 
                      last_name="chichilidze", 
                      email="nchichilidze@gmail.com", 
                      password="1234")

    buyer_a = buyer(user_id="2", 
                    name="Ranya", 
                    last_name="ElHwigi", 
                    email="ranya@gmail.com", 
                    password="1234")

    seller_art_types = ["abstract", "modern"]
    seller_a.set_art_types(seller_art_types)
    
    # add art for auction
    art_to_upload = art(art_id="1", 
                        owner_id=seller_a.get_user_id(), 
                        digital_image_path="art.jpg", 
                        description="art", 
                        art_category="modern")

    seller.add_for_exhibition(art_to_upload)
    auction = DutchAuction()
    auction.set_start_time() 
    auction.set_bid_increment()

    # mock bids 

    

