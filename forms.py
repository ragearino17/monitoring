from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min = 2, max = 20, message="Invalid Username")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min = 2, max = 20, message="Invalid Password")])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")



