from flask import Blueprint, render_template, request, redirect

import sys
sys.path.append("..")
from users.buyer import Buyer
from users.seller import seller

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password')
        accountType = request.form.get('accountType')

        if accountType == "Buyer":
            Buyer('0', first_name, last_name, email, password)
        elif accountType == "Seller":
            seller('0', first_name, last_name, email, password)

        #return redirect()


    return render_template("home.html")