import datetime
from . import db
from .auction.auction import Auction
from .art.art import Art
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required
import flask_login
from werkzeug.utils import redirect

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html")


@views.route('/rank_info')
@login_required
def rank_info():
    return render_template("rank_info.html")


@views.route('/profile')
@login_required
def profile():
    user = flask_login.current_user
    user_art = user.get_user_art()
    for art in user_art:
        print(art.get_description())

    return render_template("profile.html", user=user, user_art=user_art)


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
