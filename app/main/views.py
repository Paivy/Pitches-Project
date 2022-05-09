from flask import render_template
from app import app

#Vies
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    message = 'Place your pitch'
    title = 'Welcome to Pitches App'
    return render_template('index.html', message = message, title = title)