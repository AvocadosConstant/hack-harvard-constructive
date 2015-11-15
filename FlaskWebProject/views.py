from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from flask.ext.pymongo import PyMongo
import pymongo
'''
def mongoconn():
    MONGO_URL = "mongodb://gochoa:password1@ds042128.mongolab.com:42128/MongoLab-w"
    connection = pymongo.MongoClient(MONGO_URL)
    db = connection.get_default_database()
    print( db.collection_names())
    return db
'''
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    #mongoconn()
    return render_template(
        'index.html'
    )