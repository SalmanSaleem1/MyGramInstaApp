from flask import Blueprint, render_template, redirect, url_for, request, flash
from insta.user.forms import SignUpForm, LoginForm, SaveButtonForm
from insta.models import User, Photo
from insta import db, bcrypt
from flask_login import login_user, login_required, current_user

user = Blueprint('user', __name__)


@user.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@user.route('/signup', methods=['POST', 'GET'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.index'))
    return render_template('sign_up.html', form=form, title='Sign Up')


@user.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('user.loged_in'))
        else:
            flash(f'Login Unsuccesfull please try again', 'danger')

    return render_template('login.html', title='Login Form', form=form)


@login_required
@user.route('/loged_in', methods=['POST', 'GET'])
def loged_in():
    form = SaveButtonForm()
    if form.validate_on_submit():
        p = Photo(baseurl=fo)

    return render_template('logged_in.html', form=form)


@user.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('profile.html')


@user.route('/upload', methods=['POST', 'GET'])
def upload():
    return render_template('upload.html')
