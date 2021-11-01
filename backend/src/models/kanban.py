from extensions import db
from typing import List
from datetime import datetime
from dateutil import parser
import enum


class TaskStatus(enum.Enum):

    BACKLOG = "BACKLOG"
    TODO = "TODO"
    ONGOING = "ONGOING"
    TESTING = "TESTING"
    DONE = "DONE"


class KanbanModel(db.Model):
    __tablename__ = "kaban_tasks"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.Enum(TaskStatus), default="BACKLOG")

    def __init__(self, **kwargs):

        for key, val in kwargs.items():
            setattr(self, key, val)

    @classmethod
    def update(cls, _id, **kwargs):
        updated_task = cls.query.filter_by(id=_id).first()

        for key, val in kwargs.items():
            print(key, val)
            try:
                setattr(updated_task, key, val)
            except:
                pass

        db.session.commit()

        return updated_task

    @classmethod
    def find_by_id(cls, _id) -> "KanbanModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["KanbanModel"]:
        cls.get_count()
        return cls.query.all()

    @classmethod
    def get_count(cls) -> int:
        # print(cls.query.count())
        return cls.query.count()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
