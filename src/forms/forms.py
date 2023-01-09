from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class TodoForm(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('submit')
 
  
class TodoDescriptionForm(FlaskForm):
    description = TextAreaField('todo_descripton')
    submit = SubmitField('Submit Changes')

    def get_form_description(self, form):
        return form.description.data

    def set_form_description(self, form, description):
        form.description.data = description

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

