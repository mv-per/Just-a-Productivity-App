# import init_db
import json
import pytest


mock_kanban_tasks = [
    {
        "task": "First task",
        "description": "some1",
        "status": "BACKLOG",
    },
    {
        "task": "Second task",
        "description": "some2",
        "status": "TESTING",
    },
    {
        "task": "Third task",
        "description": "some3",
        "status": "ONGOING",
    },
]

mock_partial_kanban_task = [
    {"task": "A Partial Task", "status": "DONE"},
    {"description": "A Partial day", "status": "BACKLOG"},
]


class TestKanban:
    def test_empty_db(self, client):
        """Start with a blank database."""

        response = client.get('api/kanban/')
        assert response.status_code == 204

    @pytest.fixture
    def test_add_task(self, client):
        response = client.post('api/kanban/', json=mock_kanban_tasks[0])

        data = json.loads(response.data)
        print(data)
        assert response.status_code == 201
        assert data["id"] == 1
        assert data["task"] == mock_kanban_tasks[0]["task"]
        assert data["status"] == mock_kanban_tasks[0]["status"]
        assert data["description"] == mock_kanban_tasks[0]["description"]

    @pytest.fixture
    def test_add_multiple_tasks(self, client):
        for i in mock_kanban_tasks:
            response = client.post('api/kanban/', json=i)

    def test_get_multiple_tasks(self, client, test_add_multiple_tasks):
        response = client.get('api/kanban/')
        data = json.loads(response.data)

        assert len(data) == len(mock_kanban_tasks)
        assert response.status_code == 200

    def test_get_multiple_tasks_no_content(self, client):
        response = client.get('api/kanban/')
        # data = json.loads(response.data)
        assert len(response.data) == 0
        assert response.status_code == 204

    def test_add_and_delete_task(self, client, test_add_task):
        response = client.delete('api/kanban/1', json=mock_kanban_tasks[0])
        assert response.status_code == 202
        assert response.json["message"] == "Task Deleted successfully"

    def test_add_and_delete_task_no_task(self, client, test_add_task):
        response = client.delete('api/kanban/2', json=mock_kanban_tasks[0])
        assert response.status_code == 404
        assert response.json["message"] == "Task Not Found."

    def test_update_task(self, client, test_add_task):
        response = client.put('api/kanban/1', json=mock_kanban_tasks[1])
        print(response.data)
        assert response.status_code == 200
        data = json.loads(response.data)

        assert data["id"] == 1
        assert data["task"] == mock_kanban_tasks[1]["task"]
        assert data["status"] == mock_kanban_tasks[1]["status"]
        assert data["description"] == mock_kanban_tasks[1]["description"]

    def test_patch_task(self, client, test_add_task):
        response = client.patch(
            'api/kanban/1', json=mock_partial_kanban_task[0]
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["task"] == mock_partial_kanban_task[0]["task"]
        assert data["status"] == mock_partial_kanban_task[0]["status"]
