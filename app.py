"""
This module is the starting point for the entire app.
It imports the app and database from config and
It imports all of the routes
"""
from config import app, db
from routes import todo_list, account_auth, completed_list, profile, todo_description

if __name__ == '__main__':
    app.run(debug=True)
