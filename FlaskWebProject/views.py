"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

'''
# Flask
from flask import Flask, render_template
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', template_folder=tmpl_dir)

if __name__ == "__main__":
    app.run(debug=True)
'''