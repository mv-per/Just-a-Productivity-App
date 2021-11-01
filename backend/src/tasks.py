from flask import request
from flask_restx import Namespace, Resource

from .fields.tasks import get_task_field
from .models.tasks import TaskModel
from .schema.tasks import TaskSchema
from extensions import logger

TASK_NOT_FOUND = "Task not found."

# init namespace
api = Namespace("tasks", description="Tasks CRUD operations")

# init schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# init field
taskField = get_task_field(api)


# define routes
@api.route("/<int:taskId>")
class Task(Resource):
    @api.doc("Get a task by id")
    def get(self, taskId):
        logger.info(f"task of Id {taskId} requested")
        task = TaskModel.find_by_id(taskId)
        if task:
            return task_schema.jsonify(task)
        return {"message": TASK_NOT_FOUND}, 404

    @api.doc("Delete a Task by ID")
    def delete(self, taskId):
        task = TaskModel.find_by_id(taskId)
        if task:
            task.delete_from_db()
            logger.info(f"task of Id {taskId} deleted")
            return {"message": "Task Deleted successfully"}, 202
        return {"message": TASK_NOT_FOUND}, 404

    @api.doc("Update Task")
    @api.expect(taskField, validate=False)
    def put(self, taskId):
        task_json = request.get_json()
        updated_task = TaskModel.update(taskId, **task_json)
        logger.info(f"task of Id {taskId} updated")
        return task_schema.dump(updated_task), 200

    @api.doc("Patch task fields")
    def patch(self, taskId):
        return self.put(taskId)


@api.route("/")
class TaskList(Resource):
    @api.doc("Get all the Users")
    def get(self):
        task_list = TaskModel.find_all()
        if len(task_list) == 0:
            return tasks_schema.dump(task_list), 204
        return tasks_schema.dump(task_list), 200

    # is here because doesn't expect an ID
    @api.expect(taskField)
    @api.doc("Create a Task")
    def post(self):
        task_json = request.get_json()
        new_task = TaskModel(**task_json)
        new_task.save_to_db()
        logger.info(f"task of Id {new_task.id} added")
        return task_schema.dump(new_task), 201
