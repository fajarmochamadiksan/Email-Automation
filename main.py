from flask import Flask, render_template, request
import smtplib
import getpass

app = Flask (__name__)


# Index Static Routing
@app.route ("/", methods=["GET", "POST"])
def index ():
    
    return render_template ("index.html")

# Email Static Routing
@app.route ("/email")
def input_email ():
    return "Email Kamu"

# Profile Dinamic Routing String menggunakan %s
@app.route ("/profile/<username>")
def show_profile (username):
    return "Selamat Datang %s" % username

# ID Dinamic Routing Integer menggunakan %d
@app.route ("/blog/<int:user_id>")
def show_blog (user_id):
    return "Selamat Datang di Blog %d" % user_id

# Login Static
@app.route ("/login")
def login ():
    return render_template ("login.html")
