from flask import Flask, request
from flask.templating import render_template
from flask_mail import Mail, Message

import smtplib

# import getpass


app = Flask(__name__)

mail = Mail (app)
# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fmin51s@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ichan.161090'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Index Static Routing
@app.route('/')
def index ():
    return render_template ("index.html")

# Dashboard Dynamic Routing
@app.route('/dashboard/<username>')
def dashboard (username):
    return render_template ('dashboard.html', username=username)

# Result Static Routing
@app.route('/result', methods=['POST', 'GET'])
def result ():
    if request.method == 'POST':
        msg = Message (request.form.get("Subject", "Body"), 
                       sender='fmin51s@gmail.com', 
                       recipients=[request.form.get('Email')])
        msg.body = (request.form["Body"] + "\n\n\n\nCool Bro !!!")
        mail.send(msg)
        
        return render_template ('result.html', result="Success!")
    else :
        return render_template ('result.html', result="Send an email failure!")

if __name__ == '__main__':
    app.run (debug=True)
 





