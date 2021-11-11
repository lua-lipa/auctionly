from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/rank_info')
@login_required
def rank_info():
    return render_template("rank_info.html")