from app import app
from flask import render_template
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)



@app.route('/signup')
def signup():
    form = RegistrationForm()
    return render_template('signup.html', title="Signup", form=form)