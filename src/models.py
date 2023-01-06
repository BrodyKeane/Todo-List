from app import app, db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.Integer, Foreign_Key)
    title = db.Column(db.String(200), index = True)
    description = db.Column(db.String(1000), index = True, default = '')
    is_complete = db.Column(db.Boolean, index=True, default=False)

@app.before_first_request
def create_tables():
    db.create_all()
