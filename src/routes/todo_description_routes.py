from flask import render_template, url_for, redirect, Blueprint
from app import app
from src.forms.forms import TodoDescriptionForm
from src.database.todo_manager import TodoManager
from src.database.database_manager import DatabaseManager

todo_description_routes = Blueprint('todo_description_routes', __name__)

todo_manager = TodoManager()


@app.route('/todo/<int:id>/', methods=['GET'])
def render_todo_description(id):
    if not todo_manager.todo_exists(id):
        return redirect(url_for('todo_list'))
    todo = todo_manager.get_todo(id)
    form = get_todo_description_form(todo)
    return render_template('todo_description.html', form=form, todo=todo)

def get_todo_description_form(todo):
    description = todo_manager.get_todo_description(todo)
    form = TodoDescriptionForm()
    form.set_form_description(form, description)
    return form


@app.route('/todo/<int:id>/description', methods=['POST'])
def submit_description(id):
    form = TodoDescriptionForm()
    if form.validate_on_submit():
        todo = todo_manager.get_todo(id)
        description = form.get_form_description(form)
        todo_manager.set_todo_description(todo, description)
    return redirect(url_for('render_todo_description', id=id))