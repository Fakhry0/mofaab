# app/routes/blog.py

from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from app import db
from app.models import BlogPost, Comment
from app.forms import BlogPostForm, CommentForm
from app.decorators import admin_required  # Import the admin_required decorator
from datetime import datetime
from sqlalchemy.orm import joinedload

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blogs')
def blogs():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.paginate(page=page, per_page=5)
    return render_template('blogs.html', posts=posts)

@blog_bp.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author_id = current_user.id
        new_post = BlogPost(title=title, content=content, author_id=author_id, date_posted=datetime.utcnow())
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.blogs'))
    return render_template('add_post.html', form=form)

@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        content = form.content.data
        author_id = current_user.id
        new_comment = Comment(content=content, author_id=author_id, post_id=post.id, date_posted=datetime.utcnow())
        db.session.add(new_comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('blog.post', post_id=post.id))
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.filter_by(post_id=post.id).paginate(page=page, per_page=5)
    return render_template('post.html', post=post, form=form, comments=comments)

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

@blog_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = BlogPost.query.filter(BlogPost.title.contains(query) | BlogPost.content.contains(query)).all()
        return render_template('search_results.html', results=results)
    return render_template('search.html')
