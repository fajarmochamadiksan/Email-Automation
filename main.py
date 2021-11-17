from flask import Flask
from flask.templating import render_template
import smtplib
import getpass

app = Flask(__name__)

# Index Static Routing
@app.route('/')
def index ():
    
    return render_template ("index.html")

# Dashboard Dynamic Routing
@app.route('/dashboard')
def dashboard ():
    return render_template ('dashboard.html')






