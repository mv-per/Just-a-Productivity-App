from extensions import db
from typing import List


class TaskModel(db.Model):
    __tablename__ = "simple_tasks"

    id = db.Column(db.Integer, db.Sequence("task_id_seq"), primary_key=True)
    text = db.Column(db.String(100))
    day = db.Column(db.String(100))
    reminder = db.Column(db.Boolean())

    def __init__(self, **kwargs):
        self.text = kwargs['text']
        self.day = kwargs['day']
        self.reminder = kwargs['reminder']

    @classmethod
    def update(cls, _id, **kwargs):
        updated_task = cls.query.filter_by(id=_id).first()

        try:
            updated_task.text = kwargs['text']
        except:
            pass
        try:
            updated_task.day = kwargs['day']
        except:
            pass
        try:
            updated_task.reminder = kwargs['reminder']
        except:
            pass

        db.session.commit()

        return updated_task

    @classmethod
    def find_by_id(cls, _id) -> "TaskModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["TaskModel"]:
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
