from flask import Flask, render_template, redirect, url_for
from forms import TodoForm, AddDetailsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.static_url_path = '/static'
app.static_folder = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# create a list to store the todos
todos = []
todos_details_dict = {}
completed_todos = []

#route for main todo list
@app.route('/', methods=['GET'])
def main_list():
    return render_template('main_list.html', form=TodoForm(), todos=todos, autofocus=True)
  
#route for adding a todo. should only accept unique todos
@app.route('/submit', methods=['POST'])
def submit():
    form = TodoForm()
    if form.validate_on_submit():
        if form.todo.data not in todos_details_dict:
            todos.append(form.todo.data)
            todos_details_dict[form.todo.data] = ''
        form.todo.data = ''
    return redirect(url_for('main_list'))
  
#post route for completing todos
@app.route('/complete/<int:index>', methods=['POST'])
def complete(index):
    if index < len(todos):
        if todos[index] not in completed_todos:
            completed_todos.append(todos.pop(index))
        else:
            todos[index].pop(index)
    return redirect(url_for('main_list'))

#route to url with more info on selected todo
@app.route('/todo/<int:index>/<string:completed>', methods=['GET'])
def todo_details(index, completed):
    form = AddDetailsForm()
    print(completed)
    if completed == 'False':
        if index >= len(todos):
            return redirect(url_for('main_list'))
        else:
            form.details.data = todos_details_dict[todos[index]]
            return render_template('todo_details.html', todo=todos[index], form=form, index=index, completed=completed)
    else: 
        if index >= len(completed_todos):
            return redirect(url_for('completed_list'))
        else:
            form.details.data = todos_details_dict[completed_todos[index]]
            return render_template('todo_details.html', todo=completed_todos[index], form=form, index=index, completed=completed)
  
#adds changes to todo_details
@app.route('/todo/<int:index>/<string:completed>/add_details', methods=['POST'])
def add_details(index, completed):
    print('add_details function called')  # add debugging statement
    form = AddDetailsForm()
    if form.validate_on_submit():
        if completed == 'False':
            todos_details_dict[todos[index]] = form.details.data
        else:
            todos_details_dict[completed_todos[index]] = form.details.data
    return redirect(url_for('todo_details', index=index, completed=completed))      
  
#route to page containing all completed todosd
@app.route('/completed-list', methods=["GET"])
def completed_list():
    return render_template('completed_list.html', completed_todos=completed_todos)

#restores todo back into main list
@app.route('/completed-list/restore/<int:index>', methods=['POST'])
def restore(index):
    if index < len(completed_todos):
        todos.append(completed_todos.pop(index))
    return redirect(url_for('completed_list'))

#delted todo from list and dictionary
@app.route('/completed/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    if index < len(completed_todos):
        todos_details_dict.pop(todos[index])
        completed_todos[index].pop(index)
    return redirect(url_for('completed_list'))

if __name__ == '__main__':
    app.run(debug=True)

 