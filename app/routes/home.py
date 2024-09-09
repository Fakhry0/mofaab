from flask import Blueprint, render_template
from flask_login import current_user
from app.models import BlogPost

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('home.html', posts=posts, user=current_user)

