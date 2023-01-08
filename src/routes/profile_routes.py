from app import app, db
from src.helpers.route_helpers import try_commit, todo_exists
from flask import render_template, url_for, redirect, Blueprint

profile_routes = Blueprint('profile_routes', __name__)

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')