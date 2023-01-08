from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.helpers.route_helpers import try_commit, todo_exists, get_todo, get_completed_todos, restore_todo, add_to_session, delete_from_session

completed_list_routes = Blueprint('completed_list_routes', __name__)

@app.route('/completed-list', methods=["GET"])
def completed_list():
    completed_todos = get_completed_todos()
    return render_template('completed_list.html', completed_todos=completed_todos )
 

@app.route('/completed-list/restore/<int:id>', methods=['POST'])
def restore(id):
    if todo_exists(id):
        todo = get_todo(id)
        restore_todo(todo)
        add_to_session(todo)
        try_commit()
    return redirect(url_for('completed_list'))


@app.route('/completed/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    if todo_exists(id):
        todo = get_todo(id)
        delete_from_session(todo)
        try_commit()
    return redirect(url_for('completed_list'))