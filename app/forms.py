from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  # Username field
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email field
    password = PasswordField('Password', validators=[DataRequired()])  # Password field
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  # Confirm password field
    submit = SubmitField('Sign Up')  # Submit button

# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email field
    password = PasswordField('Password', validators=[DataRequired()])  # Password field
    remember = BooleanField('Remember Me')  # Remember me checkbox
    submit = SubmitField('Login')  # Submit button

# Project form
class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])  # Project title
    description = TextAreaField('Description', validators=[DataRequired()])  # Project description
    technologies = StringField('Technologies', validators=[DataRequired()])  # Technologies used
    link = StringField('Project Link', validators=[DataRequired()])  # Project link
    photo = FileField('Project Photo', validators=[FileAllowed(['jpg', 'png'])])  # Project photo
    submit = SubmitField('Add Project')  # Submit button

# Blog post form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])  # Post title
    content = TextAreaField('Content', validators=[DataRequired()])  # Post content
    submit = SubmitField('Post')  # Submit button

# Comment form
class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])  # Comment content
    submit = SubmitField('Add Comment')  # Submit button

# Update profile form
class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  # Username field
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email field
    about_me = TextAreaField('About Me', validators=[Length(max=500)])  # About me field
    phone_number = StringField('Phone Number', validators=[Length(max=20)])  # Phone number field
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])  # Profile picture field
    submit = SubmitField('Update Profile')  # Submit button
