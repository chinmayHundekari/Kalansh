from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
