# app/routes/blog.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import BlogPost
from app import db
from flask_login import current_user, login_required
from app.forms import BlogPostForm
from app.models import BlogPost
from app.decorators import admin_required

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

# Route to edit a blog post
@blog_bp.route('/edit-post/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_post(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('blog.post_detail', id=post.id))
    return render_template('edit_post.html', post=post)

# Route to delete a blog post
@blog_bp.route('/delete-post/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted successfully!', 'success')
    return redirect(url_for('blog.blogs'))
