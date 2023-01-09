from app import db
from src.models.models import Todo

class TodoManager:
    def create_todo(self, form):
        return Todo(title = form.todo.data)

    def complete_todo(self, todo):
        todo.is_complete = True

    def restore_todo(self, todo):
        todo.is_complete = False

    def todo_exists(self, id):
        return db.session.query(Todo).get(id) is not None

    def get_todo(self, id):
        return Todo.query.get(id)

    def get_completed_todos(self):
        return Todo.query.filter_by(is_complete = True)

    def get_uncompleted_todos(self):
        return Todo.query.filter_by(is_complete = False)

    def set_todo_description(self, form, todo):
        todo.description = form.details.data

    def set_form_details(self, form, todo):
        form.details.data = todo.description

class DatabaseManager:

    def add_to_session(self, item):
        db.session.add(item)

    def delete_from_session(self, item):
        db.session.delete(item)

    def commit(self, *args, **kwargs):
        try:
            db.session.commit(*args, **kwargs)
        except:
            db.session.rollback()

