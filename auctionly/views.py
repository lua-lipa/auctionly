import datetime
from . import db
from .auction.auction import Auction
from .art.art import Art
from .users.user import User
from flask import Blueprint, render_template, request, url_for, flash
from flask_login import login_required, current_user
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

    return render_template("profile.html", user=user)



@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_art():
    if request.method == 'POST':
        image = request.form.get('email')
        name = request.form.get('name')
        description = request.form.get('description')
        art_category = request.form.get('artCategory')
        owner_id = flask_login.current_user.id

        print(owner_id)

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

    auction_id = request.args.get('id')

    auction = Auction.query.filter_by(id=auction_id).first()

    seller = User.query.filter_by(id=auction.get_seller_id()).first()
    print(seller)
    print(auction)

    # user = flask_login.current_user

    return render_template("auction.html", auction=auction,  seller=seller)
