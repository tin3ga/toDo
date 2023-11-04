from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5

from database import engine, SessionLocal
from models import Base, Todo
import random_message
from sqlalchemy import select

Base.metadata.create_all(bind=engine)

message = random_message.greet_message()

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    with SessionLocal() as session:
        result = session.execute(select(Todo))
        tasks = result.scalars().all()
    return render_template('index.html', message=message, tasks=tasks)


@app.route("/add/", methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        with SessionLocal() as session:
            new_task = Todo(task=task, completed=False)
            session.add(new_task)
            session.commit()
        return redirect(url_for('home'))


@app.route("/completed", methods=['POST'])
def task_complete():
    task_id = request.args.get('task_id')
    with SessionLocal() as session:
        task = session.get(Todo, task_id)
        task.completed = True
        session.commit()
    return redirect(url_for('home'))


@app.route('/delete')
def delete_task():
    task_id = request.args.get('task_id')
    with SessionLocal() as session:
        task_to_delete = session.get(Todo, task_id)
        session.delete(task_to_delete)
        session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
