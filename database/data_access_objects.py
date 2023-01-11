from .models import Todo
from .database_manager import DatabaseManager

database_manager = DatabaseManager()


class TodoTable:
    def save_form_as_todo(self, form):
        todo_title = form.get_todo_title()
        new_todo = Todo(todo_title)
        database_manager.save_to_database(new_todo)
        return new_todo

    def todo_exists(self, todo_id):
        return Todo.query.get(todo_id) is not None

    def get_todo(self, todo_id):
        return Todo.query.get(todo_id)

    def get_completed_todos(self):
        return Todo.query.filter_by(is_complete = True)

    def get_uncompleted_todos(self):
        return Todo.query.filter_by(is_complete = False)






