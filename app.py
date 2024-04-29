from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

from models.database import Todo


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form['content']
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
	app.run()

