from flask import render_template, url_for, redirect
from app import db
from src.models.models import Todo
from src.forms.forms import TodoForm, AddDetailsForm


 
def todo_exists(id):
    return db.session.query(Todo).get(id) is not None


def get_todo(id):
    return Todo.query.get(id)

def get_completed_todos():
    return Todo.query.filter_by(is_complete = True)

def get_uncompleted_todos():
    return Todo.query.filter_by(is_complete = False)


def complete_todo(todo):
    todo.is_complete = True

def restore_todo(todo):
    todo.is_complete = False


def create_todo(form):
    return Todo(title = form.todo.data)


def add_to_session(item):
    db.session.add(item)

def delete_from_session(item):
    db.session.delete(item)

def try_commit(*args, **kwargs):
    try:
        db.session.commit(*args, **kwargs)
    except Exception:
        db.session.rollback()


