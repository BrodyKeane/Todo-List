from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.database.todo_manager import TodoManager
from src.database.database_manager import DatabaseManager

completed_list_routes = Blueprint('completed_list_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()
 

@app.route('/completed-list', methods=["GET"])
def render_completed_list():
    completed_todos = todo_manager.get_completed_todos()
    return render_template('completed_list.html', completed_todos=completed_todos )
 

@app.route('/completed-list/restore/<int:id>', methods=['POST'])
def restore_todo(id):
    if todo_manager.todo_exists(id): 
        todo = todo_manager.get_todo(id)
        todo_manager.restore_todo(todo)
        database_manager.add_to_session(todo)
        database_manager.commit()
    return redirect(url_for('render_completed_list'))


@app.route('/completed/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    if todo_manager.todo_exists(id):
        todo = todo_manager.get_todo(id)
        database_manager.delete_from_session(todo)
        database_manager.commit()
    return redirect(url_for('render_completed_list'))