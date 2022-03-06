from app import app,db
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data
        # ))
        # return redirect('index')
    return render_template('login.html', title='Sign In', form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulation you are now a registered user!')
        return redirect('login')
    return render_template('signup.html', title="Signup", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))