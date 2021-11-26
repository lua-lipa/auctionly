import datetime
from . import db
from .auction.auction import Auction
from .art.art import Art
from .art.art_notifications import Art_Notifications
from .users.user import User
from .system.feed import Feed
from .system.rank import Rank
from .system.ranked_user import Ranked_User
from .system.sale import Sale
from flask import Blueprint, render_template, request, url_for, flash
from flask_login import login_required
import flask_login
import base64
from werkzeug.utils import redirect

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    user = flask_login.current_user
    user_pref = user.get_user_prefs()
    feed = Feed(user_pref, flask_login.current_user.id)
    user_notifications = user.get_notification_list()
    user_auction_alerts = user.get_auction_notification_list()
    if not user_pref:
        user_feed = feed.get_feed()
    else:
        user_feed = feed.get_users_feed()
    if (request.args.get("art_id") != None):
        art_id = request.args.get('art_id')
        notify = request.args.get('notify')
        if(notify == "True"):
            attach = Art_Notifications(flask_login.current_user.id, art_id)
            db.session.add(attach)
            db.session.commit()
            user_notifications = user.get_notification_list()
            message = "You have been added to the notifications list for " +  Art.query.filter_by(id=art_id).first().get_name() + "."
            flash(message, category="success") # category="success"
        elif(notify == "False"):
            Art_Notifications.query.filter((Art_Notifications.art_id==art_id) & (Art_Notifications.user_id==flask_login.current_user.id)).delete()
            user_notifications = user.get_notification_list()
            message = "You have been removed from the notifications list for " +  Art.query.filter_by(id=art_id).first().get_name() + "."
            flash(message, category="error") # category="success"
    
    rank = Rank()
    if(user.get_user_type() == "Seller"):
        ranking = rank.get_seller_rank(flask_login.current_user.id)
        user_type = "seller"
    elif(user.get_user_type() == "Buyer"):
        ranking = rank.get_buyer_rank(flask_login.current_user.id)
        user_type = "buyer"

    if(ranking != "No rank"):
        if(ranking == "First place"):
            message = "Congratulations! You've been ranked 1st place in Auctionly's " + user_type +"'s ranking. As reward you'll recieve 30% off commission."
        if(ranking == "Second place"):
            message = "Congratulations! You've been ranked 2nd place in Auctionly's " + user_type +"'s ranking. As reward you'll recieve 20% off commission."
        if(ranking == "Third place"):
            message = "Congratulations! You've been ranked 3rd place in Auctionly's " + user_type +"'s ranking. As reward you'll recieve 10% off commission."
        flash(message, category="success") # category="success"

    return render_template("home.html", feed_art=user_feed, feed=feed, notifications=user_notifications, alerts=user_auction_alerts)


@views.route('/rank_info')
@login_required
def rank_info():
    return render_template("rank_info.html")


@views.route('/profile')
@login_required
def profile():
    user = flask_login.current_user
    user_art = user.get_user_art()
    user_auction_alerts = user.get_auction_notification_list()
    user_pref = user.get_user_prefs()
    feed = Feed(user_pref, flask_login.current_user.id)

    return render_template("profile.html", user=user, user_art=user_art, feed=feed, alerts=user_auction_alerts)


@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_art():
    if request.method == 'POST':
        name = request.form.get('name')
        owner_id = flask_login.current_user.id
        image = request.form.get('image')
        description = request.form.get('description')
        art_category = request.form.get('artCategory')

        print(owner_id)
        print(name)

        new_art = Art(name, owner_id, image, description, art_category)

        db.session.add(new_art)
        db.session.commit()

        return redirect(url_for('views.profile'))

    return render_template("upload.html")


@views.route('/auction-art', methods=['GET', 'POST'])
@login_required
def auction_art():
    if request.method == 'POST':
        art_id = request.form.get('artId')
        starting_price = request.form.get('startingPrice')
        bid_increment = request.form.get('bidIncrement')
        end_time = datetime.datetime.strptime(
            str(request.form.get('endTime')), "%Y-%m-%dT%H:%M")
        description = request.form.get('description')
        seller_id = flask_login.current_user.id

        new_auction = Auction(end_time, seller_id, art_id,
                              description, starting_price, bid_increment)

        db.session.add(new_auction)
        db.session.commit()
        art = Art.query.filter_by(id=art_id).first()
        art.up_for_auction = "True"
        db.session.commit()

    user = flask_login.current_user
    user_art = user.get_user_art()
    for art in user_art:
        print(art.get_description())

    return render_template("auction-art.html", user=user, user_art=user_art)


@views.route('/auction', methods=['GET', 'POST'])
@login_required
def auction():

    user = flask_login.current_user
    user_id = user.get_id()
    auction_id = request.args.get('id')

    auction = Auction.query.filter_by(id=auction_id).first()

    if request.method == 'POST':
        # user clicked PLACE BET
        auction.place_bid(user_id)

    print(auction)
    seller_id = auction.get_seller_id()
    seller = User.query.filter_by(id=seller_id).first()

    bids_placed_by_user = Auction.query.filter_by(seller_id=user_id).first()

    user_placed_highest_bid = False

    # need to add a check that the user has placed the highest bid

    if (bids_placed_by_user != None):
        user_placed_highest_bid = True

    return render_template("auction.html", auction=auction,  seller=seller, bid_placed=bids_placed_by_user)
