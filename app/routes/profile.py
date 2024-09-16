from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from app import db
from app.forms import UpdateProfileForm
import os
from werkzeug.utils import secure_filename

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()  # Instantiate update profile form
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        current_user.phone_number = form.phone_number.data  # Update phone number

        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)  # Save profile picture
            current_user.profile_picture = picture_file  # Update profile picture

        db.session.commit()  # Commit session
        flash('Your profile has been updated!', 'success')  # Flash success message
        return redirect(url_for('profile.profile'))  # Redirect to profile page
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
        form.phone_number.data = current_user.phone_number  # Pre-fill phone number

    profile_picture_url = url_for('static', filename='profile_pics/' + current_user.profile_picture) if current_user.profile_picture else None  # Profile picture URL

    return render_template('profile.html', form=form, profile_picture_url=profile_picture_url)  # Render profile template

def save_picture(form_picture):
    random_hex = os.urandom(8).hex()  # Generate random hex
    _, f_ext = os.path.splitext(form_picture.filename)  # Get file extension
    picture_fn = random_hex + f_ext  # Create picture filename
    picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picture_fn)  # Create picture path
    form_picture.save(picture_path)  # Save picture to path
    return picture_fn  # Return picture filename

@profile_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    form = UpdateProfileForm()  # Instantiate update profile form
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data  # Update about me
        current_user.phone_number = form.phone_number.data  # Update phone number

        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)  # Save profile picture
            current_user.profile_picture = picture_file  # Update profile picture

        db.session.commit()  # Commit session
        flash('Your profile has been updated!', 'success')  # Flash success message
        return redirect(url_for('profile.profile'))  # Redirect to profile page
    return render_template('profile.html', user=current_user, form=form)  # Render profile template
