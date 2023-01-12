"""
This module provides functionality for todo descriptions in the app.
It defines three main routes:
- '/todo/<int:todo_id>' route for rendering a template displaying the todo's
    description
- '/todo/<int:todo_id>/submit' route for handling the submission of new
    descriptions
It uses a blueprint to group related routes together and make the code more organized.
It makes use of a TodoTable Data Access Object (DAO) class to perform database operations
and a DatabaseManager class to handle the connection and management of the database.
It also uses a TodoForm class for validating the input data before submitting to the server.
It makes use of Flask's render_template, redirect, and url_for functions.
"""
from flask import render_template, url_for, redirect, Blueprint

from config import app
from forms.forms import TodoDescriptionForm
from database.data_access_objects import TodoTable
from database.database_manager import DatabaseManager

todo_description_routes = Blueprint('todo_description_routes', __name__)
todo_table = TodoTable()
database_manager = DatabaseManager()


@app.route('/todo/<int:todo_id>/', methods=['GET'])
def render_todo_description(todo_id):
    """
        Renders description page for todos

    Args:
        todo_id (int): id for todo in database

    Returns:
        html page with todo description form
    """
    if not todo_table.todo_exists(todo_id):
        return redirect(url_for('todo_list'))
    todo = todo_table.get_todo(todo_id)
    form = TodoDescriptionForm.get_form_with_description(todo)
    return render_template('todo_description.html', form=form, todo=todo)


@app.route('/todo/<int:todo_id>/description', methods=['POST'])
def submit_description(todo_id):
    """
        Handles description submition from user

    Args:
        todo_id (int): id for todo in database

    Returns:
        redirects back to description page
    """
    form = TodoDescriptionForm()
    if form.validate_on_submit():
        todo_table.save_todo_description(todo_id, form)
    return redirect(url_for('render_todo_description', todo_id=todo_id))
