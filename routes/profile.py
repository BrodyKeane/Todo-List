from flask import render_template, Blueprint

from config import app

profile_routes = Blueprint('profile_routes', __name__)


@app.route('/profile', methods=['GET'])
def render_profile():
    return render_template('profile.html')