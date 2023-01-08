from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.models.models import Todo
from src.forms.forms import TodoForm
from src.helpers.route_helpers import try_commit, todo_exists, get_todo

todo_list_routes = Blueprint('todo_list_routes', __name__)

@app.route('/todo-list', methods=['GET'])
def todo_list():
    todos = Todo.query.filter_by(is_complete = False)
    return render_template('todo_list.html', form=TodoForm(), todos=todos, autofocus=True)


@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(title = form.todo.data)
        db.session.add(new_todo)
        try_commit()
        form.todo.data = ''
    return redirect(url_for('todo_list'))


@app.route('/complete/<int:id>', methods=['POST'])
def complete(id):
    if todo_exists(id):
        todo = get_todo(id)
        todo.is_complete = True
        db.session.add(todo)
        try_commit()
    return redirect(url_for('todo_list'))