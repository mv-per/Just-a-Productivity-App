# Model required by flask_restx for expect


from flask_restx import fields
from ..models.kanban import TaskStatus


def kanban_field(api):
    TaskKanbanField = api.model(
        'KanbanModel',
        {
            # 'id': fields.Integer(),
            'task': fields.String('Task name'),
            'description': fields.String('Task Description'),
            'status': fields.String(
                description='The Task Status',
                enum=[x.name for x in TaskStatus],
            ),
        },
    )

    return TaskKanbanField
