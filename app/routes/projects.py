# mofaab/app/routes/projects.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegistrationForm, LoginForm, ProjectForm
from ..models import Project
from .. import db

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('projects.html', projects=all_projects)

@projects_bp.route('/project/<int:id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('project_detail.html', project=project)

@projects_bp.route('/add-project', methods=['GET', 'POST'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            technologies=form.technologies.data,
            link=form.link.data
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('projects.projects'))
    return render_template('project_form.html', form=form)

@projects_bp.route('/edit-project/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        project.technologies = form.technologies.data
        project.link = form.link.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('projects.project_detail', id=project.id))
    return render_template('project_form.html', form=form)
