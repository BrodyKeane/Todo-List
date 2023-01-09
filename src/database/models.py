from app import app, db
from datetime import datetime
from flask_login import UserMixin

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200), index = True)
    description = db.Column(db.String(1000), index = True, default = '')
    is_complete = db.Column(db.Boolean, index=True, default=False)
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('todo', uselist=False))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_todos = db.Column(db.Integer, index=True, default=0)
    total_uncompleted_todos = db.Column(db.Integer, index=True, default=0)
    total_completed_todos = db.Column(db.Integer, index=True, default=0)
    todo_completion_rate = db.Column(db.Float, index=True, default=0)
    
    user = db.relationship('User', backref=db.backref('stats', uselist=False))
    


@app.before_first_request
def create_tables():
    db.create_all()