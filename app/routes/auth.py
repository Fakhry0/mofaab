from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))  # Redirect if already authenticated
    form = RegistrationForm()  # Instantiate registration form
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Set password
        db.session.add(new_user)  # Add new user to session
        db.session.commit()  # Commit session
        flash('Your account has been created! You are now able to log in', 'success')  # Flash success message
        return redirect(url_for('auth.login'))  # Redirect to login page
    return render_template('signup.html', form=form)  # Render signup template

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))  # Redirect if already authenticated
    form = LoginForm()  # Instantiate login form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Fetch user by email
        if user and user.check_password(form.password.data):  # Check password
            login_user(user, remember=form.remember.data)  # Log in user
            next_page = request.args.get('next')  # Get next page
            return redirect(next_page) if next_page else redirect(url_for('home.home'))  # Redirect to next page or home
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')  # Flash error message
    return render_template('login.html', form=form)  # Render login template

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Log out user
    flash('You have been logged out.', 'success')  # Flash success message
    return redirect(url_for('auth.login'))  # Redirect to login page
