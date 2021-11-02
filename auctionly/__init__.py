from flask import Flask
from users import seller
from users import buyer 
from art import art 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alkjsfkalalfks'

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

def mock_users(): 
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

    art_to_upload = art(art_id="1", 
                        owner_id=seller_a.get_user_id(), 
                        digital_image_path="art.jpg", 
                        description="art", 
                        art_category="modern")

    seller.add_for_exhibition(art_to_upload)

    # mock auction
    # mock bids 

    
