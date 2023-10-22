from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import datetime
import random

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, unique=True, nullable=False)
    completed = db.Column(db.Boolean,nullable=False)


weekday = ["Monday 😛",
           "Tuesday 🍒",
           "Wednesday 😬",
           "Thursday 🥱",
           "Friday 🍻",
           "Saturday 🤗",
           "Sunday 😴"]
random_word = [
    "Hello, it's ",
    "Hey, it's ",
    "Smile, it's ",
    "Warm wishes, it's ",
    "Wonderful, it's ",
    "Wishing you a fantastic ",
    "Sending you a big hug, it's ",
    "Have an amazing "
]


def greet_message():
    today = datetime.date.today().weekday()
    message = f'{random.choice(random_word)} {weekday[today]}'
    return message


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"

db.init_app(app)
with app.app_context():
    db.create_all()

message = greet_message()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Task))
        tasks = result.scalars().all()
    return render_template('index.html', message=message, tasks=tasks)


@app.route("/add/", methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        with app.app_context():
            new_task = Task(task=task, completed=False)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('home'))


@app.route("/completed",methods=['POST'])
def task_complete():
    task_id = request.args.get('task_id')
    with app.app_context():
        task = db.get_or_404(Task, task_id)
        task.completed = True
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete')
def delete_task():
    task_id = request.args.get('task_id')
    with app.app_context():
        task_to_delete = db.get_or_404(Task, task_id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
