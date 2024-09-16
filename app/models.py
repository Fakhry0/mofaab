from datetime import datetime
from app import db
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(150), nullable=False, unique=True)  # Username field
    email = db.Column(db.String(150), nullable=False, unique=True)  # Email field
    password_hash = db.Column(db.String(128))  # Password hash field
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag
    about_me = db.Column(db.Text, nullable=True)  # About me field
    phone_number = db.Column(db.String(20), nullable=True)  # Phone number field
    profile_picture = db.Column(db.String(200), nullable=True)  # Profile picture field
    posts = db.relationship('BlogPost', backref='author', lazy=True)  # Relationship to BlogPost
    comments = db.relationship('Comment', backref='author', lazy=True)  # Relationship to Comment

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # Set password hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # Check password hash

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Project title
    description = db.Column(db.Text, nullable=False)  # Project description
    technologies = db.Column(db.String(200), nullable=False)  # Technologies used
    link = db.Column(db.String(200), nullable=False)  # Project link
    photo = db.Column(db.String(20), nullable=True)  # Project photo
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date created

    def __repr__(self):
        return f"Project('{self.title}', '{self.date_created}')"  # String representation

# BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Post title
    content = db.Column(db.Text, nullable=False)  # Post content
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date posted
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User
    comments = db.relationship('Comment', backref='post', lazy=True)  # Relationship to Comment

# Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    content = db.Column(db.Text, nullable=False)  # Comment content
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date posted
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User
    post_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'), nullable=False)  # Foreign key to BlogPost

    def __repr__(self):
        return f'<Comment {self.content}>'  # String representation

# Author model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(50))  # Author name
    profile_picture_url = db.Column(db.String(200))  # Profile picture URL
