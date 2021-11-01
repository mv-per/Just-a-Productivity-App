from extensions import db
from typing import List
from datetime import datetime
from dateutil import parser


class TaskModel(db.Model):
    __tablename__ = "simple_tasks"

    id = db.Column(db.Integer, db.Sequence("task_id_seq"), primary_key=True)
    name = db.Column(db.String(100))
    day = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
    description = db.Column(db.Text)
    reminder = db.Column(db.Boolean())

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.day = parser.isoparse(kwargs['day'])
        self.description = kwargs['description']
        self.reminder = kwargs['reminder']

    # def _convertDate(self, date):
    #     return datetime.date.strptime(date, '%Y-%m-%d')

    @classmethod
    def update(cls, _id, **kwargs):
        updated_task = cls.query.filter_by(id=_id).first()

        try:
            updated_task.name = kwargs['name']
        except:
            pass
        try:
            updated_task.day = parser.isoparse(kwargs['day'])
        except:
            pass
        try:
            updated_task.reminder = kwargs['reminder']
        except:
            pass

        try:
            updated_task.description = kwargs['description']
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
