from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from flask import Flask
from flask.ext.pymongo import PyMongo
import pymongo

def mongoconn():
    MONGO_URL = "mongodb://bloomingwaters2:bloomingwaters2@ds042128.mongolab.com:42128/MongoLab-w"
    connection = pymongo.MongoClient(MONGO_URL)
    db = connection.get_default_database()
    print( db.collection_names())
    return db

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    mongoconn()
    return "DSLKJD"
    return render_template(
        'index.html'
    )
