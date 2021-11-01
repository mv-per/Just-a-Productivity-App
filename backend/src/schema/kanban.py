from marshmallow.utils import EXCLUDE
from extensions import ma
from ..models.kanban import KanbanModel

from marshmallow_enum import EnumField
from marshmallow import fields
import enum


class Status(enum.Enum):
    BACKLOG = "BACKLOG"
    TODO = "TODO"
    ONGOING = "ONGOING"
    TESTING = "TESTING"
    DONE = "DONE"

    def __str__(self):
        return self.value


class KanbanSchema(ma.SQLAlchemyAutoSchema):

    status = EnumField(Status, by_value=True, many=False)

    class Meta:
        # fields = ("task", "description", "status")
        model = KanbanModel
        # exclude = ("id",)
