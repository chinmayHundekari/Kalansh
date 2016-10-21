from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title="Kalansh"
    user = {'name': 'Chinmay Hundekari'};
    notes = [
            {
                'title' : 'Note 1',
                'content' : 'Note 1 Content'
            },
            {
                'title' : 'Note 2',
                'content' : 'Note 2 Content'
            },
            {
                'title' : 'Note 3',
                'content' : 'Note 3 Content'
            },
            {
                'title' : 'Note 4',
                'content' : 'Note 4 Content'
            }
            ]
    return render_template("index.html",
            title=title,
            user=user,
            notes=notes)
