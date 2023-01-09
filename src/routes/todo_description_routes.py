from flask import render_template, url_for, redirect, Blueprint
from app import app
from src.forms.forms import TodoDescriptionForm
from src.helpers.route_helpers import TodoManager, DatabaseManager, FormManager

todo_description_routes = Blueprint('todo_description_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()
form_manager = FormManager()

@app.route('/todo/<int:id>/', methods=['GET'])
def todo_description(id):
    form = TodoDescriptionForm()
    if todo_manager.todo_exists(id):
        todo = todo_manager.get_todo(id)
        description = todo_manager.get_todo_description(todo)
        form.set_form_description(form, description)
        return render_template('todo_description.html', form=form, todo=todo)
    else:
        return redirect(url_for('todo_list'))

@app.route('/todo/<int:id>/description', methods=['POST'])
def add_description(id):
    form = TodoDescriptionForm()
    if form.validate_on_submit():
        todo = todo_manager.get_todo(id)
        description = form.get_form_description(form)
        todo_manager.set_todo_description(todo, description)
        database_manager.add_to_database(todo)
    return redirect(url_for('todo_description', id=id))