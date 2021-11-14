from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
import flask_login
from werkzeug.utils import redirect

views = Blueprint('views', __name__)

from .art.art import Art
from . import db



@views.route('/')
@login_required
def home():
    return render_template("home.html")


@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

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
        db.session.flush()
        new_art.set_art_id(new_art.id)

        return redirect(url_for('views.profile'))


    return render_template("upload.html")
