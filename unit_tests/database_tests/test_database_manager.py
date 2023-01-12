import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Todo, Base
from database.database_manager import DatabaseManager



class DatabaseManagerTest(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///test.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)
        self.database_manager = DatabaseManager()

    def test_save_to_database_on_new(self):
        todo = Todo(title='Test Todo')
        self.database_manager.save_to_database(self.session, todo)

        # check if the todo was added to the database
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertEqual(result, todo)

    def test_save_to_database_on_existing(self):
        todo = Todo(title='Test Todo')
        self.database_manager.save_to_database(self.session, todo)
        todo.set_description('This is a test todo')
        self.database_manager.save_to_database(self.session, todo)

        #check if todo was updated in database
        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertEqual(result.description, 'This is a test todo')

    def test_remove_from_session(self):
        todo = Todo(title='Test Todo')
        self.database_manager.save_to_database(self.session, todo)
        self.database_manager.remove_from_database(self.session, todo)

        result = self.session.query(Todo).filter_by(title='Test Todo').first()
        self.assertEqual(result, None)
    

    def tearDown(self):
        # remove test data and drop the test database tables
        self.session.query(Todo).delete()
        self.session.commit()
        self.session.close()
        self.engine.dispose()
