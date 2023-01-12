"""
This module creates the database for the todo list app
It creates three tables:
- 'Todo' The Todo table is used to store information about each individual todo
- 'User' The User table contains the users account info and links their todos
   and stats
- 'Stats' The Stats table contains the users stats related to their todo history

Datetime is user to keep records of dates
UserMixin is imported from flask_login to help with the User table
The app and database are imported from config so they can be directly accessed
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from flask_login import UserMixin

from config import app, db

Base = declarative_base()

class Todo(Base):
    """
    Table for containing todo data. Only accepts title on initialization.

    Todo Table:
        -id: Primary key for all todos

        -user_id: Foreign key that like to the user that owns the todo

        -title: Title of the todo

        -description: Description of the todo if given

        -is_complete: Boolean state of todo
    """
    __tablename__ = 'Todo'
    id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200), index = True)
    description = db.Column(db.String(1000), index = True, default = '')
    is_complete = db.Column(db.Boolean, index=True, default=False)

    # user = db.relationship('User', backref=db.backref('todo', uselist=False))

    def __init__(self, title):
        """
        Creates Todo object

        Args:
            title (string): title of todo
        """
        self.title = title
        self.description = ''
        self.is_complete = False

    def set_description(self, description):
        """
        Updates the todo description
        """
        self.description = description

    def complete(self):
        """
        Marks the todo as complete
        """
        self.is_complete = True

    def restore(self):
        """
        Marks the todo as uncomplete
        """
        self.is_complete = False


# class User(UserMixin, Base):
#     """Incomplete"""
#     __tablename__ = 'User'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)


# class Stats(Base):
#     """Incomplete"""
#     __tablename__ = 'Stats'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     total_todos = db.Column(db.Integer, index=True, default=0)
#     total_uncompleted_todos = db.Column(db.Integer, index=True, default=0)
#     total_completed_todos = db.Column(db.Integer, index=True, default=0)
#     todo_completion_rate = db.Column(db.Float, index=True, default=0)

#     user = db.relationship('User', backref=db.backref('stats', uselist=False))


@app.before_first_request
def create_tables():
    """Creates the tables before the first request is made"""
    engine = create_engine('sqlite:///todoDB.db')
    Base.metadata.create_all(bind=engine)
