"""
This module Generates form templates for use inside routes.
It defines three main form classes:
- 'TodoForm' is used for recieving new todos from a user on the todo_list page
- 'TodoDescriptionForm' is used for recieving descriptions for the users todos
   on the todo description page
- 'RegistrationForm' Incomplete

The forms inherit FlaskForm from flask_wtf.
The forms get their fields from wtforms
and a DatabaseManager class to handle the connection and management of the database.
They also get their validators from wtforms.validators
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class TodoForm(FlaskForm):

    """
    Contains a todo stringfield and a submit field
    This form inherits from FlaskForm and uses wtforms to create its form
    fields. The data also gets validated with wtforms.validators
    """
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('submit')

    def get_todo_title(self):
        """
        Returns data the user put into the todo field
        """
        return self.todo.data


class TodoDescriptionForm(FlaskForm):
    """
    Contains a description TextAreaField and a submit field
    This form inherits from FlaskForm and uses wtforms to create its form
    fields. The data also gets validated with wtforms.validators
    """
    description = TextAreaField('todo_descripton')
    submit = SubmitField('Submit Changes')

    @classmethod
    def get_form_with_description(cls, todo):
        """
        Takes discription from todo and makes it the descriptions default value

        Args:
            todo (object): Todo class

        Returns:
            form: contains stored description
        """
        description = todo.description
        form = cls()
        form.set_description(description)
        return form

    def get_description(self):
        """
        Gets description from form
        """
        return self.description.data

    def set_description(self, description):
        """
        Sets form's default description
        """
        self.description.data = description


class RegistrationForm(FlaskForm):
    """Incomplete"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
