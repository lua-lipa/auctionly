from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

#from .models import User
from .users.buyer import Buyer
from .users.seller import Seller
from .users.user import User
from .users.user_preference import UserPreference
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                print("logged in")
                login_user(user, remember=True)
            else:
                print("incorrect password")
        else:
            print("email not found")

        return redirect(url_for('views.home'))

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password')
        accountType = request.form.get('accountType')
        StillLife = request.form.get("Still Life") != None
        Landscape = request.form.get("Landscape") != None
        Seascape = request.form.get("Seascape") != None
        Portraiture = request.form.get("Portraiture") != None
        Abstract = request.form.get("Abstract") != None
        
        if len(first_name) < 4:
            flash("First name must be greater than 3 characters.", category="error") # category="success"
        else:
            flash("Account Created")

            # user = User(email=email, first_name=first_name, last_name=last_name, password=password)
            # db.session.add(user)
            # db.session.commit()
            # db.session.flush()
            # user_id = user.id

            user = None

            if accountType == "Buyer":
                user = Buyer(first_name, last_name, email, password)
            elif accountType == "Seller":
                user = Seller(first_name, last_name, email, password)

            db.session.add(user)
            db.session.commit()
            db.session.flush()
            user.set_user_id(user.id)

            login_user(user, remember=True)

            user_id = user.get_user_id()
            user_db = User.query.filter_by(id=user_id).first()
            if isinstance(user, Seller):
                user_db.user_type = "Seller"
            elif isinstance(user, Buyer):
                user_db.user_type = "Buyer"
            
            db.session.commit()

            if StillLife:
                pref = UserPreference(user_id, "Still Life")
                db.session.add(pref)
                db.session.commit()
            if Landscape:
                pref = UserPreference(user_id, "Landscape")
                db.session.add(pref)
                db.session.commit()
            if Seascape:
                pref = UserPreference(user_id, "Seascape")
                db.session.add(pref)
                db.session.commit()
            if Portraiture:
                pref = UserPreference(user_id, "Portraiture")
                db.session.add(pref)
                db.session.commit()
            if Abstract:
                pref = UserPreference(user_id, "Abstract")
                db.session.add(pref)
                db.session.commit()

            return redirect(url_for('views.home'))


    return render_template("signup.html")