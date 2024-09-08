from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.decorators import admin_required
from app.models import User, Project, BlogPost
from app import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/admin/users')
@login_required
@admin_required
def manage_users():
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@admin_bp.route('/admin/projects')
@login_required
@admin_required
def manage_projects():
    projects = Project.query.all()
    return render_template('admin/manage_projects.html', projects=projects)

@admin_bp.route('/admin/blog_posts')
@login_required
@admin_required
def manage_blog_posts():
    blog_posts = BlogPost.query.all()
    return render_template('admin/manage_blog_posts.html', blog_posts=blog_posts)
