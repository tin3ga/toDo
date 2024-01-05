from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from flask_login import UserMixin
from todo.db.database import SessionLocal


class Base(DeclarativeBase):
    pass


class User(Base, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    todos = relationship('Todo', backref='user')

    def __repr__(self) -> str:
        return f"user={self.user_id}"

    def add_todo(self, task):
        with SessionLocal() as session:
            new_task = Todo(task=task, user_id=self.id, completed=False)
            session.add(new_task)
            session.commit()

    def task_complete(self, task_id):
        with SessionLocal() as session:
            task = session.get(Todo, task_id)
            task.completed = True
            session.commit()

    def delete_task(self, task_id):
        with SessionLocal() as session:
            task_to_delete = session.get(Todo, task_id)
            session.delete(task_to_delete)
            session.commit()


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    task: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(nullable=False)


