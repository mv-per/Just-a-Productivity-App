from extensions import ma
from src.models.tasks import TaskModel


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields = ('text', 'day', 'reminder')
        model = TaskModel
