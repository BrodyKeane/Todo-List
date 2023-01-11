from config import app, db
from routes import todo_list, account_auth, completed_list, profile, todo_description

if __name__ == '__main__':
    app.run(debug=True)
