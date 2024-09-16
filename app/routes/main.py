from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import ProjectForm
from app.models import Project
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return render_template('home.html')  # Render home page

@main_bp.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    form = ProjectForm()  # Instantiate project form
    if form.validate_on_submit():
        project = Project(title=form.title.data, description=form.description.data, owner=current_user)  # Create new project
        db.session.add(project)  # Add project to session
        db.session.commit()  # Commit session
        flash('Project added successfully!', 'success')  # Flash success message
        return redirect(url_for('main.projects'))  # Redirect to projects page
    
    user_projects = Project.query.all()  # Fetch all projects
    return render_template('projects.html', form=form, projects=user_projects)  # Render projects template
