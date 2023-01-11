from app import db
from .models import Todo
from .database_manager import DatabaseManager

database_manager = DatabaseManager()

class TodoManager:
    def create_todo(self, form):
        return Todo(form.todo.data)

    def todo_exists(self, todo_id):
        return db.session.query(Todo).get(todo_id) is not None

    def get_todo(self, todo_id):
        return Todo.query.get(todo_id)

    def get_completed_todos(self):
        return Todo.query.filter_by(is_complete = True)

    def get_uncompleted_todos(self):
        return Todo.query.filter_by(is_complete = False)







