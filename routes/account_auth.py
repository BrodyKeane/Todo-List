from flask import render_template, url_for, redirect, Blueprint

from config import app

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