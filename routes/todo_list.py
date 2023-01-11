"""
This module provides functionality for managing todo items in a web application.
It defines three main routes:
- '/todo-list' route for rendering a template displaying the list of todos
- '/submit' route for handling the submission of new todos
- '/complete/<int:todo_id>' route for handling the completion of existing todos.

It uses a blueprint to group related routes together and make the code more organized.
It makes use of a TodoTable Data Access Object (DAO) class to perform database operations
and a DatabaseManager class to handle the connection and management of the database.
It also uses a TodoForm class for validating the input data before submitting to the server.
It makes use of Flask's render_template, redirect, and url_for functions.
"""
from flask import render_template, url_for, redirect, Blueprint

from config import app
from forms.forms import TodoForm
from database.data_access_objects import TodoTable
from database.database_manager import DatabaseManager

todo_list_routes = Blueprint('todo_list_routes', __name__)
todo_table = TodoTable()
database_manager = DatabaseManager()


@app.route('/todo-list', methods=['GET'])
def render_todo_list():
    """
    Renders the todo list page.
    The function uses TodoForm to generate the form and uses the todo_table
    data access object to retrieve all of the users uncompleted todos from the
    database
    """
    form = TodoForm()
    todos = todo_table.get_uncompleted_todos()
    return render_template('todo_list.html', form=form, todos=todos)


@app.route('/submit', methods=['POST'])
def submit_todo():
    """
    Handle the submission of a new todo by a user.
    The function uses the TodoForm for validating the input and saves the new
    todo to the database using the TodoTable Data Access Object, and then
    redirects to the '/todo-list' route.
    """
    form = TodoForm()
    if form.validate_on_submit():
        todo_table.save_form_as_todo(form)
    return redirect(url_for('render_todo_list'))


@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id): 
    """
    Handle the completion of an existing todo by the user.
    The function uses the todo_table data access object to complete the todo
    within the database.
    """
    if todo_table.todo_exists(todo_id):
        todo_table.complete_todo(todo_id)
    return redirect(url_for('render_todo_list'))
