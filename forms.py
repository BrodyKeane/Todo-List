from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# create a WTForm to handle user input for adding new todos
class TodoForm(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('submit')
 
  
class AddDetailsForm(FlaskForm):
    details = TextAreaField('todo_details')
    submit = SubmitField('Submit Changes')

