from flask_restx import Api

from .tasks import api as task_ns

api_description = """   
    A Simple Task API
    """

api = Api(
    title="A Simple Task API",
    version="1.0",
    description=api_description,
    doc='/docs',
    contact="mav.pereira@outlook.com",
)

api.add_namespace(task_ns, path='/api/tasks')
