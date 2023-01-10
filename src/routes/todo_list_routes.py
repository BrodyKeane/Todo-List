from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.forms.forms import TodoForm
from src.database.query import TodoManager
from src.database.database_manager import DatabaseManager
from src.database.models import Todo

todo_list_routes = Blueprint('todo_list_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()

@app.route('/todo-list', methods=['GET'])
def render_todo_list():
    form = TodoForm()
    todos = todo_manager.get_uncompleted_todos()
    return render_template('todo_list.html', form=form, todos=todos, autofocus=True)
 

@app.route('/submit', methods=['POST'])
def submit_todo():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = todo_manager.create_todo(form)
        database_manager.add_to_database(new_todo)
    return redirect(url_for('render_todo_list'))


@app.route('/complete/<int:id>', methods=['POST'])
def complete_todo(id):
    if todo_manager.todo_exists(id):
        todo = todo_manager.get_todo(id)
        todo.complete()
        database_manager.add_to_database(todo)
    return redirect(url_for('render_todo_list'))