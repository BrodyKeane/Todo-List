from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.helpers.route_helpers import commit_changes, todo_exists

completed_list_routes = Blueprint('completed_list_routes', __name__)

@app.route('/completed-list', methods=["GET"])
def completed_list():
    completed_todos = Todo.query.filter_by(is_complete = True)
    return render_template('completed_list.html', completed_todos=completed_todos )


@app.route('/completed-list/restore/<int:id>', methods=['POST'])
def restore(id):
    if todo_exists(id):
        todo = Todo.query.get(id)
        todo.is_complete = False
        commit_changes()
    return redirect(url_for('completed_list'))


@app.route('/completed/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    if todo_exists(id):
        todo = Todo.query.get(id)
        db.session.delete(todo)
        commit_changes()
    return redirect(url_for('completed_list'))