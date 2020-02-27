from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l(
        'Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset Password'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class RegistrationForm(FlaskForm):
    """Registration
    
    Parameters
    ----------
    FlaskForm : Form
        User registration form
    
    Raises
    ------
    ValidationError
        Username is required
    ValidationError
        Passwords must match
    """
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired(), Length(min=8, max=20)])
    password2 = PasswordField(_l(
        'Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_("Username has already been taken!"))
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is  not None:
            raise ValidationError(_("Email already in use!"))



class LoginForm(FlaskForm):
    username = StringField(_l("Username"), validators=[(DataRequired())])
    password = PasswordField(_l("Passsword"), validators=[(DataRequired())])
    remember_me = BooleanField(_l("Remember me"))
    submit = SubmitField(_l("Sign In"))
    


