from flask import render_template, url_for, redirect, Blueprint
from app import app
from src.forms.forms import TodoDescriptionForm
from src.database.query import TodoManager
from src.database.database_manager import DatabaseManager
from src.database.models import Todo

todo_description_routes = Blueprint('todo_description_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()

@app.route('/todo/<int:id>/', methods=['GET'])
def render_todo_description(id):
    if not todo_manager.todo_exists(id):
        return redirect(url_for('todo_list'))
    todo = todo_manager.get_todo(id)
    form = get_todo_description_form(todo)
    return render_template('todo_description.html', form=form, todo=todo)

def get_todo_description_form(todo):
    description = todo.get_description()
    form = TodoDescriptionForm()
    form.set_description(description)
    return form


@app.route('/todo/<int:id>/description', methods=['POST'])
def submit_description(id):
    form = TodoDescriptionForm()
    if form.validate_on_submit():
        todo = todo_manager.get_todo(id)
        description = form.get_description()
        todo.set_description(description)
        database_manager.add_to_database(todo)
    return redirect(url_for('render_todo_description', id=id))