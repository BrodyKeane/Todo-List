import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Todo

class TodoTest(unittest.TestCase):
    def setUp(self):
        # create a test database and tables
        self.engine = create_engine('sqlite:///test.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_todo(self):
        # test creating a new todo
        todo = Todo(title='Test Todo')
        self.session.add(todo)
        self.session.commit()

        # check if the todo was added to the database
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertEqual(result, todo)

    def test_set_description(self):
        # test setting the description of a todo
        todo = Todo(title='Test Todo')
        todo.set_description('This is a test todo')
        self.session.add(todo)
        self.session.commit()

        # check if the description was set correctly
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertEqual(result.description, 'This is a test todo')

    def test_complete_todo(self):
        # test marking a todo as complete
        todo = Todo(title='Test Todo')
        todo.complete()
        self.session.add(todo)
        self.session.commit()

        # check if the todo was marked as complete
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertTrue(result.is_complete)

    def test_restore_todo(self):
        # test marking a todo as uncomplete
        todo = Todo(title='Test Todo')
        todo.complete()
        todo.restore()
        self.session.add(todo)
        self.session.commit()

        # check if the todo was marked as uncomplete
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertFalse(result.is_complete)

    def tearDown(self):
        # remove test data and drop the test database tables
        self.session.query(Todo).delete()
        self.session.commit()
        self.session.close()
        self.engine.dispose()

