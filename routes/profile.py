from flask import render_template, url_for, redirect, Blueprint
from config import app, db
from database.query import TodoManager
from database.database_manager import DatabaseManager

profile_routes = Blueprint('profile_routes', __name__)


@app.route('/profile', methods=['GET'])
def render_profile():
    return render_template('profile.html')