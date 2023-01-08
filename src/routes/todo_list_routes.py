from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import TodoForm
from src.helpers.route_helpers import try_commit, todo_exists, get_todo, get_uncompleted_todos, create_todo, add_to_session, complete_todo

todo_list_routes = Blueprint('todo_list_routes', __name__)

@app.route('/todo-list', methods=['GET'])
def todo_list():
    form = TodoForm()
    todos = get_uncompleted_todos()
    return render_template('todo_list.html', form=form, todos=todos, autofocus=True)


@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = create_todo(form)
        add_to_session(new_todo)
        try_commit()
    return redirect(url_for('todo_list'))


@app.route('/complete/<int:id>', methods=['POST'])
def complete(id):
    if todo_exists(id):
        todo = get_todo(id)
        complete_todo(todo)
        add_to_session(todo)
        try_commit()
    return redirect(url_for('todo_list'))