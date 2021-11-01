from flask import request
from flask_restx import Namespace, Resource


from .fields.kanban import kanban_field
from .models.kanban import KanbanModel
from .schema.kanban import KanbanSchema

TASK_NOT_FOUND = "Task Not Found."

# init namespace
api = Namespace("kanban", description="Kanban CRUD operations")


# init schemas
kanban_schema = KanbanSchema()
kanbans_schema = KanbanSchema(many=True)

# init fields
kanbanField = kanban_field(api)


# define routes
@api.route("/<int:taskId>")
class KanbanTask(Resource):
    @api.doc("Get an Task by id")
    def get(self, taskId):
        task = KanbanModel.find_bytaskId(taskId)
        if task:
            return kanban_schema.jsonify(task)
        return {"message": TASK_NOT_FOUND}, 404

    @api.doc("Delete an task by ID")
    def delete(self, taskId):
        task = KanbanModel.find_by_id(taskId)
        if task:
            task.delete_from_db()
            return {"message": "Task Deleted successfully"}, 202
        return {"message": TASK_NOT_FOUND}, 404

    @api.doc("Update Task")
    @api.expect(kanbanField, validate=True)
    def put(self, taskId):
        task = KanbanModel.find_by_id(taskId)
        if task:
            task_json = request.get_json()
            updated_task = KanbanModel.update(taskId, **task_json)
            return kanban_schema.dump(updated_task), 200
        return {"message": TASK_NOT_FOUND}, 404

    @api.doc("Patch task fields")
    def patch(self, taskId):
        task = KanbanModel.find_by_id(taskId)
        if task:
            return self.put(taskId)
        else:
            return {"message": TASK_NOT_FOUND}, 404


@api.route("/")
class KanbanTaskList(Resource):
    @api.doc("Get all Kanban Tasks")
    def get(self):
        task_list = KanbanModel.find_all()
        if len(task_list) == 0:
            return kanbans_schema.dump(task_list), 204
        return kanbans_schema.dump(task_list)

    # is here because doesn't expect an ID
    @api.expect(kanbanField, validate=True)
    @api.doc("Create a kanban Task")
    def post(self):
        task_json = request.get_json()
        new_task = KanbanModel(**task_json)
        new_task.save_to_db()
        return kanban_schema.dump(new_task), 201
