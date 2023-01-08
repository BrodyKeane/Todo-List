from flask import render_template, url_for, redirect
from app import app, db
from src.models.models import Todo
from src.forms.forms import TodoForm, AddDetailsForm


def commit_changes(*args, **kwargs):
    try:
        db.session.commit(*args, **kwargs)
    except Exception as e:
        db.session.rollback()
        # raise e


def todo_exists(id):
    return db.session.query(Todo).get(id) is not None