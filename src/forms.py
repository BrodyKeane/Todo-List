from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

# create a WTForm to handle user input for adding new todos
class TodoForm(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('submit')
 
  
class AddDetailsForm(FlaskForm):
    details = TextAreaField('todo_details')
    submit = SubmitField('Submit Changes')


class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

