from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import AddDetailsForm
from src.helpers.route_helpers import try_commit, todo_exists, get_todo, set_form_details, set_todo_description, add_to_session

todo_details_routes = Blueprint('todo_details_routes', __name__)

@app.route('/todo/<int:id>/', methods=['GET'])
def todo_details(id):
    form = AddDetailsForm()
    if todo_exists(id):
        todo = get_todo(id)
        set_form_details(form, todo)
        return render_template('todo_details.html', form=form, todo=todo)

    return redirect(url_for('todo_list'))




@app.route('/todo/<int:id>/add_details', methods=['POST'])
def add_details(id):
    form = AddDetailsForm()
    if form.validate_on_submit():
        todo = get_todo(id)
        set_todo_description(form, todo)
        add_to_session(todo)
        try_commit()
    return redirect(url_for('todo_details', id=id))     