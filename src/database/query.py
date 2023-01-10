from app import db
from src.database.models import Todo
from src.database.database_manager import DatabaseManager

database_manager = DatabaseManager()

class TodoManager:

    def create_todo(form):
        return Todo(form.details.data)

    def todo_exists(self, id):
        return db.session.query(Todo).get(id) is not None

    def get_todo(self, id):
        return Todo.query.get(id)

    def get_completed_todos(self):
        return Todo.query.filter_by(is_complete = True)

    def get_uncompleted_todos(self):
        return Todo.query.filter_by(is_complete = False)







