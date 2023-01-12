"""
This module is responsible for all updates to the database
It imports the database directly from config
"""
from config import db


class DatabaseManager:
    """
    Responsible for all updates to the database
    """
    def save_to_database(self, item):
        """
        Directly saves item to database
        """
        self.add_to_session(item)
        self.commit()

    def remove_from_database(self, item):
        """
        Directly removes item from
        """
        self.remove_from_session(item)
        self.commit()

    def add_to_session(self, item):
        """
        Adds item to the current session
        """
        db.session.add(item)

    def remove_from_session(self, item):
        """
        Removes the item from the session
        """
        db.session.delete(item)

    def commit(self, *args, **kwargs):
        """
        Trys to commit all session changes to database if they are valaid
        """
        try:
            db.session.commit(*args, **kwargs)
        except:
            db.session.rollback()
            