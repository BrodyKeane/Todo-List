from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import app, db
from src.models import Todo
from src.forms import TodoForm, AddDetailsForm


#temporary storage to mimic db
todos = []
todos_details_dict = {}
completed_todos = []


'''
Routes for "main_list.html"
'''

#route for uncompleted todos
@app.route('/', methods=['GET'])
def main_list():
    todos = Todo.query.filter_by(is_complete = False)
    return render_template('main_list.html', form=TodoForm(), todos=todos, autofocus=True)

#route for adding a todo to db
@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(title = form.todo.data)
        db.session.add(new_todo)
        commit_changes()
        form.todo.data = ''
    return redirect(url_for('main_list'))

#route for completing todos
@app.route('/complete/<int:id>', methods=['POST'])
def complete(id):
    if todo_exists(id):
        todo = Todo.query.get(id)
        todo.is_complete = True
        db.session.add(todo)
        commit_changes()
    return redirect(url_for('main_list'))

'''
Routes for "todo_details.html"
'''

#route to url with more info on selected todo
@app.route('/todo/<int:id>/', methods=['GET'])
def todo_details(id):
    form = AddDetailsForm()
    if not todo_exists(id):
        return redirect(url_for('main_list'))
    else:
        todo=Todo.query.get(id)
        form.details.data = todo.description
        return render_template('todo_details.html', form=form, todo=todo)
  
#adds changes to todo_details
@app.route('/todo/<int:id>/add_details', methods=['POST'])
def add_details(id):
    form = AddDetailsForm()
    if form.validate_on_submit():
        todo = Todo.query.get(id)
        todo.description = form.details.data
        db.session.add(todo)
        commit_changes()
    return redirect(url_for('todo_details', id=id))      

'''
Routes for "completed_list.html"
'''

#route to page containing all completed todos
@app.route('/completed-list', methods=["GET"])
def completed_list():
    completed_todos = Todo.query.filter_by(is_complete = True)
    return render_template('completed_list.html', completed_todos=completed_todos )

#restores todo back into main list
@app.route('/completed-list/restore/<int:id>', methods=['POST'])
def restore(id):
    if todo_exists(id):
        todo = Todo.query.get(id)
        todo.is_complete = False
        commit_changes()
    return redirect(url_for('completed_list'))

#delted todo from list and dictionary
@app.route('/completed/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    if todo_exists(id):
        todo = Todo.query.get(id)
        db.session.delete(todo)
        commit_changes()
    return redirect(url_for('completed_list'))

'''
helper functions for db
'''

def commit_changes(*args, **kwargs):
    try:
        db.session.commit(*args, **kwargs)
    except Exception as e:
        db.session.rollback()
        # raise e


def todo_exists(id):
    return db.session.query(Todo).get(id) is not None

if __name__ == '__main__':
    app.run(debug=True)