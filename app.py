from flask import Flask, render_template, redirect, url_for, request
from forms import TodoForm, AddDetailsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.static_url_path = '/static'
app.static_folder = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# create a list to store the todos
todos = []
todos_details_dict = {}
  
def get_icons():
    return {
        'unchecked': url_for('static', filename='icons/unchecked.png'),
        'checked': url_for('static', filename='icons/checked.png')
    }
        
#route for main todo list
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', form=TodoForm(), todos=todos, icon_urls=get_icons(), autofocus=True)

#route for adding a todo. should only accept unique todos
@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        if form.todo.data not in todos:
            todos.append(form.todo.data)
            todos_details_dict[form.todo.data] = ''
        form.todo.data = ''
    return redirect(url_for('index'))

#post route for deleting todos
@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if index < len(todos):
        del todos[index]
    return redirect(url_for('index'))
 
#route to url with more info on selected todo
@app.route('/todo/<int:index>', methods=['GET'])
def todo_details(index):
    form = AddDetailsForm()
    if index >= len(todos):
        return redirect(url_for('index'))
    return render_template('todo_details.html', todo=todos[index], details=todos_details_dict[todos[index]], form=form, index=index)

#adds changes to todo_details
@app.route('/todo/<int:index>/add_details', methods=['POST'])
def add_details(index):
    if request.method == 'POST':
        request.form['text'] = '' 
    return redirect(url_for('todo_details', index=index))
 
  
if __name__ == '__main__':
    app.run(debug=True)

