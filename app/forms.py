from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    technologies = StringField('Technologies', validators=[DataRequired()])
    link = StringField('Project Link', validators=[DataRequired()])
    photo = FileField('Project Photo', validators=[FileAllowed(['jpg', 'png'])])  # Add the photo field
    submit = SubmitField('Add Project')

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Add Comment')

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    about_me = TextAreaField('About Me', validators=[Length(max=500)])
    phone_number = StringField('Phone Number', validators=[Length(max=20)])  # Add phone number field
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])  # Add profile picture field
    submit = SubmitField('Update Profile')
