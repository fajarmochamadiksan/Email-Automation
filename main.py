from flask import Flask
app = Flask(__name__)

# Index Routing
@app.route('/')
def index ():
    return "Hallo"
