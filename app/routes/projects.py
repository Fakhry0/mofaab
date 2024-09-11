# mofaab/app/routes/projects.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.forms import RegistrationForm, LoginForm, ProjectForm
from ..models import Project
from .. import db
from app.decorators import admin_required

projects_bp = Blueprint('projects', __name__)

# Display all projects (accessible by everyone)
@projects_bp.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('projects.html', projects=all_projects)

# Display project details (accessible by everyone)
@projects_bp.route('/project/<int:id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('project_detail.html', project=project)

# Add new project (admin only)
@projects_bp.route('/add-project', methods=['GET', 'POST'])
@login_required
@admin_required
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        photo_file = None
        if form.photo.data:
            photo_file = save_picture(form.photo.data)  # Save the photo file
        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            technologies=form.technologies.data,
            link=form.link.data,
            photo=photo_file  # Save the photo filename to the database
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('projects.projects'))
    return render_template('project_form.html', form=form)

# Edit existing project (admin only)
@projects_bp.route('/edit-project/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    if not current_user.is_admin:
        abort(403)
    if form.validate_on_submit():
        if form.photo.data:
            project.photo = save_picture(form.photo.data)  # Save the new photo file
        project.title = form.title.data
        project.description = form.description.data
        project.technologies = form.technologies.data
        project.link = form.link.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('projects.project_detail', id=project.id))
    return render_template('project_form.html', form=form)

import os
from flask import current_app
from werkzeug.utils import secure_filename

def save_picture(form_picture):
    random_hex = os.urandom(8).hex()
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picture_fn)
    form_picture.save(picture_path)
    return picture_fn
