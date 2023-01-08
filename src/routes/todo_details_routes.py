from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import AddDetailsForm
from src.helpers.route_helpers import commit_changes, todo_exists

todo_details_routes = Blueprint('todo_details_routes', __name__)

@app.route('/todo/<int:id>/', methods=['GET'])
def todo_details(id):
    form = AddDetailsForm()
    if not todo_exists(id):
        return redirect(url_for('todo_list'))
    else:
        todo=Todo.query.get(id)
        form.details.data = todo.description
        return render_template('todo_details.html', form=form, todo=todo)
  

@app.route('/todo/<int:id>/add_details', methods=['POST'])
def add_details(id):
    form = AddDetailsForm()
    if form.validate_on_submit():
        todo = Todo.query.get(id)
        todo.description = form.details.data
        db.session.add(todo)
        commit_changes()
    return redirect(url_for('todo_details', id=id))     