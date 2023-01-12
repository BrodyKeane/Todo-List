"""
This module is responsible for all updates to the database
It imports the database directly from config
"""
from config import db


class DatabaseManager:
    """
    Responsible for all updates to the database
    """
    def save_to_database(self, session, item):
        """
        Directly saves item to database
        """
        self.add_to_session(session, item)
        self.commit(session)

    def remove_from_database(self, session, item):
        """
        Directly removes item from
        """
        self.remove_from_session(session, item)
        self.commit(session)

    def add_to_session(self, session, item):
        """
        Adds item to the current session
        """
        session.add(item)

    def remove_from_session(self, session, item):
        """
        Removes the item from the session
        """
        session.delete(item)

    def commit(self, session, *args, **kwargs):
        """
        Trys to commit all session changes to database if they are valaid
        """
        try:
            session.commit(*args, **kwargs)
        except:
            session.rollback()
            