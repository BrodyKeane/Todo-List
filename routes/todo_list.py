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
    form = TodoForm()
    todos = todo_table.get_uncompleted_todos()
    return render_template('todo_list.html', form=form, todos=todos, autofocus=True)


@app.route('/submit', methods=['POST'])
def submit_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo_table.save_form_as_todo(form)
    return redirect(url_for('render_todo_list'))


@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    if todo_table.todo_exists(todo_id):
        todo = todo_table.get_todo(todo_id)
        todo.complete()
        database_manager.save_to_database(todo)
    return redirect(url_for('render_todo_list'))
