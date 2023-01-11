from .models import Todo
from .database_manager import DatabaseManager

database_manager = DatabaseManager()


class TodoTable:
    def save_form_as_todo(self, form):
        todo_title = form.get_todo_title()
        new_todo = Todo(todo_title)
        database_manager.save_to_database(new_todo)
        return new_todo

    def save_todo_description(self, todo_id, form):
        todo = self.get_todo(todo_id)
        description = form.get_description()
        todo.set_description(description)
        database_manager.save_to_database(todo)

    def complete_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        todo.complete()
        database_manager.save_to_database(todo)

    def restore_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        todo.restore()
        database_manager.save_to_database(todo)

    def delete_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        database_manager.remove_from_database(todo)

    def todo_exists(self, todo_id):
        return Todo.query.get(todo_id) is not None

    def get_todo(self, todo_id):
        return Todo.query.get(todo_id)

    def get_completed_todos(self):
        return Todo.query.filter_by(is_complete = True)

    def get_uncompleted_todos(self):
        return Todo.query.filter_by(is_complete = False)

