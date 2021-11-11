from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login")
def login_signup():
    return render_template('login.html')


@app.route("/feed")
def feed():
    return "Feed"


@app.route("/profile")
def profile():
    return "Profile"
    

if __name__ == "__main__":
    app.run(debug=True)
