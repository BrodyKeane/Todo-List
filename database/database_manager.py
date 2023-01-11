from config import db


class DatabaseManager:
    def add_to_session(self, item):
        db.session.add(item)

    def remove_from_session(self, item):
        db.session.delete(item)

    def commit(self, *args, **kwargs):
        try:
            db.session.commit(*args, **kwargs)
        except:
            db.session.rollback()

    def save_to_database(self, item):
        self.add_to_session(item)
        self.commit()

    def remove_from_database(self, item):
        self.remove_from_session(item)
        self.commit()
