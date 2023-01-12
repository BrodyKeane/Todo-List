"""
This module provides functionality for managing completed todo items in the app.
It defines three main routes:
- '/completed-list' route for rendering a template displaying the list of
    completed todos
- '/completed-list/restore/<int:todo_id>' route for restoring a todo to its
    uncompleted status
- '/completed/delete/<int:todo_id> ' route for handling the deletion of
    completed todos.

It uses a blueprint to group related routes together and make the code more organized.
It makes use of a TodoTable Data Access Object (DAO) class to perform database operations
and a DatabaseManager class to handle the connection and management of the database.
It makes use of Flask's render_template, redirect, and url_for functions.
"""
from flask import render_template, url_for, redirect, Blueprint

from config import app
from database.database_manager import DatabaseManager
from database.data_access_objects import TodoTable

completed_list_routes = Blueprint('completed_list_routes', __name__)
todo_table = TodoTable()
database_manager = DatabaseManager()


@app.route('/completed-list', methods=["GET"])
def render_completed_list():
    """
    Renders list of the users completed todos
    """
    completed_todos = todo_table.get_completed_todos()
    return (
        render_template('completed_list.html', completed_todos=completed_todos)
    )

@app.route('/completed-list/restore/<int:todo_id>', methods=['POST'])
def restore_todo(todo_id):
    """
        Restores a todo back to an uncomplete status

    Args:
        todo_id (int): id for todo in database

    Returns:
        redirect: render_completed_list route
    """
    if todo_table.todo_exists(todo_id):
        todo_table.restore_todo(todo_id)
    return redirect(url_for('render_completed_list'))


@app.route('/completed/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """
    Deletes a todo from the database

    Args:
        todo_id (int): id for todo in database

    Returns:
        redirect: render_completed_list route
    """
    if todo_table.todo_exists(todo_id):
        todo_table.delete_todo(todo_id)
    return redirect(url_for('render_completed_list'))
