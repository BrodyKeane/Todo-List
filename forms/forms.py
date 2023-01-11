"""Generates form templates for use inside routes"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class TodoForm(FlaskForm):
    """Generates form for inputting a new todo"""
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('submit')

    def get_todo_title(self):
        """Returns data the user put into the todo field"""
        return self.todo.data
 
  
class TodoDescriptionForm(FlaskForm):
    """Generate form for inputting a todo's description"""
    description = TextAreaField('todo_descripton')
    submit = SubmitField('Submit Changes')

    @classmethod
    def get_form_with_description(cls, todo):
        description = todo.description
        form = cls()
        form.set_description(description)
        return form

    def get_description(self):
        return self.description.data

    def set_description(self, description):
        self.description.data = description


class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register') 
