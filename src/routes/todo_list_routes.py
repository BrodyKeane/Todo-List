from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.forms.forms import TodoForm
from src.helpers.route_helpers import TodoManager, DatabaseManager

todo_list_routes = Blueprint('todo_list_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()

@app.route('/todo-list', methods=['GET'])
def todo_list():
    form = TodoForm()
    todos = todo_manager.get_uncompleted_todos()
    return render_template('todo_list.html', form=form, todos=todos, autofocus=True)
 

@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = todo_manager.create_todo(form)
        database_manager.add_to_session(new_todo)
        database_manager.commit()
    return redirect(url_for('todo_list'))


@app.route('/complete/<int:id>', methods=['POST'])
def complete(id):
    if todo_manager.todo_exists(id):
        todo = todo_manager.get_todo(id)
        todo_manager.complete_todo(todo)
        database_manager.add_to_session(todo)
        database_manager.commit()
    return redirect(url_for('todo_list'))