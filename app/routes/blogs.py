from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from app.models import BlogPost

blogs_bp = Blueprint('blogs', __name__)

@blogs_bp.route('/blogs')
def blogs():
    # Query to retrieve all blog posts
    blog_posts = BlogPost.query.all()
    return render_template('blogs.html', blogs=blog_posts)

@blogs_bp.route('/blogs/<int:blog_id>')
def blog_detail(blog_id):
    # Query to retrieve a specific blog post by ID
    blog_post = BlogPost.query.get(blog_id)

    if blog_post is None:
        flash('Blog post not found.', 'danger')
        return redirect(url_for('blogs.blogs'))

    return render_template('blog_detail.html', blog=blog_post)
