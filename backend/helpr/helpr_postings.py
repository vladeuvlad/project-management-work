"""
The main body of routes for the application. Handle the creation, updating, and access of postings.
"""
from helpr import app, db


@app.route('/')
def hello_world():
    return 'It Lives!'
