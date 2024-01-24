import os

from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, current_user
from sqlalchemy import select

from db.database import engine, SessionLocal
from db.models import Base, User
from utils import random_message
from utils.generate_uuid import generate_uuid

Base.metadata.create_all(bind=engine)

message = random_message.greet_message()

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = os.environ["SECRET_KEY"]

# Flask Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as session:
        return session.query(User).get(int(user_id))


@app.route('/')
def register_uuid():
    unique_uuid: str = generate_uuid()
    with SessionLocal() as session:
        result = session.execute(select(User)).scalars()
        if unique_uuid not in [users.user_id for users in result]:
            new_user = User(user_id=unique_uuid)
            session.add(new_user)
            session.commit()
            login_user(new_user)

    return redirect(url_for('home', unique_uuid=unique_uuid))


@app.route('/T<unique_uuid>')
def home(unique_uuid):
    tasks: list = []
    with SessionLocal() as session:
        result = session.execute(select(User)).scalars()
        if unique_uuid not in [users.user_id for users in result]:
            new_user = User(user_id=unique_uuid)
            session.add(new_user)
            login_user(new_user)
            session.commit()
        else:
            user = session.query(User).filter_by(user_id=unique_uuid).first()
            login_user(user)
            for todo in user.todos:
                tasks.append(todo)

    return render_template('index.html', message=message, unique_uuid=unique_uuid, tasks=tasks)


@app.route("/add/", methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task: str = request.form.get('task')
        unique_uuid: str = current_user.user_id
        with SessionLocal() as session:
            result = session.execute(select(User).where(User.id == current_user.id))
            user = result.scalar()
            user.add_todo(task=task)
        return redirect(url_for('home', unique_uuid=unique_uuid))


@app.route("/completed", methods=['POST'])
def task_complete():
    task_id: str = request.args.get('task_id')
    unique_uuid: str = current_user.user_id
    with SessionLocal() as session:
        result = session.execute(select(User).where(User.id == current_user.id))
        user = result.scalar()
        user.task_complete(task_id=task_id)
    return redirect(url_for('home', unique_uuid=unique_uuid))


@app.route('/delete')
def delete_task():
    task_id: str = request.args.get('task_id')
    unique_uuid: str = current_user.user_id
    with SessionLocal() as session:
        result = session.execute(select(User).where(User.id == current_user.id))
        user = result.scalar()
        user.delete_task(task_id=task_id)
        return redirect(url_for('home', unique_uuid=unique_uuid))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
