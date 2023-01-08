from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import AddDetailsForm
from src.helpers.route_helpers import try_commit, todo_exists, get_todo

todo_details_routes = Blueprint('todo_details_routes', __name__)

@app.route('/todo/<int:id>/', methods=['GET'])
def todo_details(id):
    form = AddDetailsForm()
    if not todo_exists(id):
        return redirect(url_for('todo_list'))
    else:
        todo = get_todo(id)
        form.details.data = todo.description
        return render_template('todo_details.html', form=form, todo=todo)
  

@app.route('/todo/<int:id>/add_details', methods=['POST'])
def add_details(id):
    form = AddDetailsForm()
    if form.validate_on_submit():
        todo = get_todo(id)
        todo.description = form.details.data
        db.session.add(todo)
        try_commit()
    return redirect(url_for('todo_details', id=id))     