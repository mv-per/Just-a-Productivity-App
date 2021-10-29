# Model required by flask_restx for expect


from flask_restx import fields


def get_task_field(api):
    TaskField = api.model(
        'TaskModel',
        {
            'id': fields.Integer(),
            'text': fields.String('Tasks TO-DO'),
            'day': fields.String('Due Date'),
            'reminder': fields.Boolean(),
        },
    )

    return TaskField
