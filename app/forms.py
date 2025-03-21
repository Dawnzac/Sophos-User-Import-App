from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UserImportForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    group = SelectField('Group', choices=[('students', 'Students'), ('admins', 'Admins')], validators=[DataRequired()])
    add_user = SubmitField('Add User')