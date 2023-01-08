from app import app, db
from src.models.models import Todo
from src.forms.forms import TodoForm, AddDetailsForm
from src.helpers.route_helpers import commit_changes, todo_exists
from flask import render_template, url_for, redirect, Blueprint


account_auth_routes = Blueprint('account_auth_routes', __name__)

@app.route('/')
def root():
    return redirect(url_for('todo_list'))


@app.route('/sign-up', methods=['GET'])
def sign_up():
    return render_template('sign_up.html')


@app.route('/sign-in', methods=['GET'])
def sign_in():
    return render_template('sign_in.html')