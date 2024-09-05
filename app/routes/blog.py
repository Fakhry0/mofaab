# app/routes/blog.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import BlogPost
from app import db
from flask_login import current_user, login_required
from app.forms import BlogPostForm

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blogs')
def blogs():
    posts = BlogPost.query.order_by(BlogPost.date_created.desc()).all()
    return render_template('blogs.html', posts=posts)

@blog_bp.route('/post/<int:id>')
def post_detail(id):
    post = BlogPost.query.get_or_404(id)
    return render_template('blog_detail.html', post=post)

@blog_bp.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('blog.blogs'))
    return render_template('add_post.html', form=form)
