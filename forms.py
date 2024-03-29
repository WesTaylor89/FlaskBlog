from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken, '
                                  'Please try again')

    def validate_email(self, email):
        email = User.query.filter_by(username=email.data).first()
        if email:
            raise ValidationError('That email is already in use, '
                                  'Please try again')


class LoginForm(FlaskForm):
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken, '
                                      'Please try again')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(username=email.data).first()
            if email:
                raise ValidationError('That email is already in use, '
                                      'Please try again')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
