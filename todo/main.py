from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, current_user
from sqlalchemy import select
from uuid import uuid4

from todo.db.database import engine, SessionLocal
from todo.db.models import Base, User
from todo.utils import random_message

Base.metadata.create_all(bind=engine)

message = random_message.greet_message()

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Flask Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as session:
        return session.query(User).get(int(user_id))


def generate_url() -> str:
    unique_url: str = str(uuid4())
    unique_url = unique_url.replace("-", "")
    return unique_url


@app.route('/')
def register_uuid():
    unique_url: str = generate_url()
    with SessionLocal() as session:
        result = session.execute(select(User)).scalars()
        if unique_url not in [users.user_id for users in result]:
            new_user = User(user_id=unique_url)
            session.add(new_user)
            session.commit()
            login_user(new_user)

    return redirect(url_for('home', unique_url=unique_url))


@app.route('/<unique_url>')
def home(unique_url):
    tasks: list = []
    with SessionLocal() as session:
        result = session.execute(select(User)).scalars()
        if unique_url not in [users.user_id for users in result]:
            new_user = User(user_id=unique_url)
            session.add(new_user)
            session.commit()
        else:
            user = session.query(User).filter_by(user_id=unique_url).first()
            for todo in user.todos:
                tasks.append(todo)

    return render_template('index.html', message=message, unique_url=unique_url, tasks=tasks)


@app.route("/add/", methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task: str = request.form.get('task')
        unique_url: str = current_user.user_id
        with SessionLocal() as session:
            result = session.execute(select(User).where(User.id == current_user.id))
            user = result.scalar()
            user.add_todo(task=task)
        return redirect(url_for('home', unique_url=unique_url))


@app.route("/completed", methods=['POST'])
def task_complete():
    task_id: str = request.args.get('task_id')
    unique_url: str = current_user.user_id
    with SessionLocal() as session:
        result = session.execute(select(User).where(User.id == current_user.id))
        user = result.scalar()
        user.task_complete(task_id=task_id)
    return redirect(url_for('home', unique_url=unique_url))


@app.route('/delete')
def delete_task():
    task_id: str = request.args.get('task_id')
    unique_url: str = current_user.user_id
    with SessionLocal() as session:
        result = session.execute(select(User).where(User.id == current_user.id))
        user = result.scalar()
        user.delete_task(task_id=task_id)
        return redirect(url_for('home', unique_url=unique_url))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
