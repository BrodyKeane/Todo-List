"""
This module is responsible for all public access to database
The TodoTable data access object gives access to the Todo objects in the database

The models and database modules are imported to handle all database intereraction.
"""
from .models import Todo
from .database_manager import DatabaseManager
from config import db

database_manager = DatabaseManager()

class TodoTable:
    """
    The data access object for the Todo table
    """
    def save_form_as_todo(self, form):
        """
        Takes title from form and stores it as a todo

        Args:
            form (object): TodoForm

        Returns:
            object: Todo
        """
        todo_title = form.get_todo_title()
        new_todo = Todo(todo_title)
        database_manager.save_to_database(new_todo)
        return new_todo

    def save_todo_description(self, todo_id, form):
        """
        Stores new description inside database

        Args:
            todo_id (int): Id for todo in database
            form (Object): Contains description provided by user
        """
        todo = self.get_todo(todo_id)
        description = form.get_description()
        todo.set_description(description)
        database_manager.save_to_database(todo)

    def complete_todo(self, todo_id):
        """
        Marks the todo as complete and updates the database
        """
        todo = self.get_todo(todo_id)
        todo.complete()
        database_manager.save_to_database(todo)

    def restore_todo(self, todo_id):
        """
        Marks the todo as uncomplete and updates the database
        """
        todo = self.get_todo(todo_id)
        todo.restore()
        database_manager.save_to_database(todo)

    def delete_todo(self, todo_id):
        """
        removes the todo from the database
        """
        todo = self.get_todo(todo_id)
        database_manager.remove_from_database(todo)

    def todo_exists(self, todo_id):
        """
        if the todo exists returns True; else returns False
        """
        return db.session.query(Todo).get(todo_id) is not None


    def get_todo(self, todo_id):
        """
        Gets the todo object from the database
        """
        return db.session.query(Todo).get(todo_id)

    def get_completed_todos(self):
        """
        Gets all of the users completed todos from the database
        """
        return db.session.query(Todo).filter_by(is_complete = True).all()

    def get_uncompleted_todos(self):
        """
        Gets all of the users uncompleted todos from the database
        """
        return db.session.query(Todo).filter_by(is_complete=False).all()
