# import init_db
import json
import pytest

mock_tasks = [
    {
        "name": "First task",
        "day": "2021-10-07T00:00:00",
        "description": "some1",
        "reminder": False,
    },
    {
        "name": "Second task",
        "day": "2021-10-07T00:00:00",
        "description": "some2",
        "reminder": True,
    },
    {
        "name": "Third task",
        "day": "2021-10-07T00:00:00",
        "description": "some3",
        "reminder": False,
    },
]

mock_partial_task = [
    {"name": "A Partial Task", "day": "2021-10-07T00:00:00"},
    {"day": "A Partial day", "reminder": True},
]


def test_empty_db(client):
    """Start with a blank database."""

    response = client.get('api/tasks/')
    print(response)
    assert response.status_code == 204


@pytest.fixture
def test_add_task(client):
    response = client.post('api/tasks/', json=mock_tasks[0])

    data = json.loads(response.data)
    print(data)
    assert response.status_code == 201
    assert data["id"] == 1
    assert data["name"] == mock_tasks[0]["name"]
    assert data["day"] == mock_tasks[0]["day"]
    assert data["description"] == mock_tasks[0]["description"]
    assert data["reminder"] == mock_tasks[0]["reminder"]


@pytest.fixture
def test_add_multiple_tasks(client):
    for i in mock_tasks:
        response = client.post('api/tasks/', json=i)


def test_get_multiple_tasks(client, test_add_multiple_tasks):
    response = client.get('api/tasks/')
    data = json.loads(response.data)

    assert len(data) == len(mock_tasks)
    assert response.status_code == 200


def test_get_multiple_tasks_no_content(client):
    response = client.get('api/tasks/')
    # data = json.loads(response.data)
    print(response.data)
    assert len(response.data) == 0
    assert response.status_code == 204


def test_add_and_delete_task(client, test_add_task):
    response = client.delete('api/tasks/1', json=mock_tasks[0])
    assert response.status_code == 202
    assert response.json["message"] == "Task Deleted successfully"


def test_add_and_delete_task_no_task(client, test_add_task):
    response = client.delete('api/tasks/2', json=mock_tasks[0])
    assert response.status_code == 404
    assert response.json["message"] == "Task not found."


def test_update_task(client, test_add_task):
    response = client.put('api/tasks/1', json=mock_tasks[1])

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id"] == 1
    assert data["name"] == mock_tasks[1]["name"]
    assert data["day"] == mock_tasks[1]["day"]
    assert data["description"] == mock_tasks[1]["description"]
    assert data["reminder"] == mock_tasks[1]["reminder"]


def test_patch_task(client, test_add_task):
    response = client.patch('api/tasks/1', json=mock_partial_task[0])
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == mock_partial_task[0]["name"]
    assert data["day"] == mock_partial_task[0]["day"]
