from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.database.models import Todo
from src.forms.forms import TodoForm, TodoDescriptionForm
from src.database.todo_manager import TodoManager
from src.database.database_manager import DatabaseManager



account_auth_routes = Blueprint('account_auth_routes', __name__)

@app.route('/')
def root():
    return redirect(url_for('render_todo_list'))


@app.route('/sign-up', methods=['GET'])
def render_sign_up():
    return render_template('sign_up.html')


@app.route('/sign-in', methods=['GET'])
def render_sign_in():
    return render_template('sign_in.html')