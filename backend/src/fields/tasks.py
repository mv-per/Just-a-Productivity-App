# Model required by flask_restx for expect


from flask_restx import fields


def get_task_field(api):
    TaskField = api.model(
        'TaskModel',
        {
            # 'id': fields.Integer(),
            'name': fields.String('Task name'),
            'day': fields.DateTime(),
            'description': fields.String('Task Description'),
            'reminder': fields.Boolean(),
        },
    )

    return TaskField
