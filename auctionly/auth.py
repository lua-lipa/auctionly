from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from .models import User
from .users.buyer import Buyer
from .users.seller import Seller
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
        print(accountType)

        print("sign up")

        user = User(email=email, first_name=first_name, last_name=last_name, password=password)
        db.session.add(user)
        db.session.commit()
        db.session.flush()
        user_id = user.id

        if accountType == "Buyer":
            Buyer(user_id, first_name, last_name, email, password)
        elif accountType == "Seller":
            Seller(user_id, first_name, last_name, email, password)

        login_user(user, remember=True)
        return redirect(url_for('views.home'))


    return render_template("signup.html")