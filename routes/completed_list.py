from flask import render_template, url_for, redirect, Blueprint
from app import app
from database.database_manager import DatabaseManager
from database.query import TodoManager

completed_list_routes = Blueprint('completed_list_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()


@app.route('/completed-list', methods=["GET"])
def render_completed_list():
    completed_todos = todo_manager.get_completed_todos()
    return render_template('completed_list.html', completed_todos=completed_todos )


@app.route('/completed-list/restore/<int:todo_id>', methods=['POST'])
def restore_todo(todo_id):
    if todo_manager.todo_exists(todo_id):
        todo = todo_manager.get_todo(todo_id)
        todo.restore()
        database_manager.add_to_database(todo)
    return redirect(url_for('render_completed_list'))

@app.route('/completed/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    if todo_manager.todo_exists(todo_id):
        todo = todo_manager.get_todo(todo_id)
        database_manager.remove_from_database(todo)
    return redirect(url_for('render_completed_list'))