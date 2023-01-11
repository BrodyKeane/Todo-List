from flask import render_template, url_for, redirect, Blueprint
from app import app
from forms.forms import TodoDescriptionForm
from database.query import TodoManager
from database.database_manager import DatabaseManager

todo_description_routes = Blueprint('todo_description_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()

@app.route('/todo/<int:todo_id>/', methods=['GET'])
def render_todo_description(todo_id):
    if not todo_manager.todo_exists(todo_id):
        return redirect(url_for('todo_list'))
    todo = todo_manager.get_todo(todo_id)
    form = get_todo_description_form(todo)
    return render_template('todo_description.html', form=form, todo=todo)

def get_todo_description_form(todo):
    description = todo.description
    form = TodoDescriptionForm()
    form.set_description(description)
    return form

@app.route('/todo/<int:todo_id>/description', methods=['POST'])
def submit_description(todo_id):
    form = TodoDescriptionForm()
    if form.validate_on_submit():
        todo = todo_manager.get_todo(todo_id)
        description = form.get_description()
        todo.description = description
        database_manager.add_to_database(todo)
    return redirect(url_for('render_todo_description', todo_id=todo_id))
