from flask import render_template, url_for, redirect, Blueprint
from app import app, db
from src.database.todo_manager import TodoManager
from src.database.database_manager import DatabaseManager


profile_routes = Blueprint('profile_routes', __name__)

@app.route('/profile', methods=['GET'])
def render_profile():
    return render_template('profile.html')