from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import AddDetailsForm
from src.helpers.route_helpers import TodoManager, DatabaseManager

todo_details_routes = Blueprint('todo_details_routes', __name__)
todo_manager = TodoManager()
database_manager = DatabaseManager()

@app.route('/todo/<int:id>/', methods=['GET'])
def todo_details(id):
    form = AddDetailsForm()
    if todo_manager.todo_exists(id):
        todo = todo_manager.get_todo(id)
        todo_manager.set_form_details(form, todo)
        return render_template('todo_details.html', form=form, todo=todo)

    return redirect(url_for('todo_list'))

@app.route('/todo/<int:id>/add_details', methods=['POST'])
def add_details(id):
    form = AddDetailsForm()
    if form.validate_on_submit():
        todo = todo_manager.get_todo(id)
        todo_manager.set_todo_description(form, todo)
        database_manager.add_to_session(todo)
        database_manager.commit()
    return redirect(url_for('todo_details', id=id))     