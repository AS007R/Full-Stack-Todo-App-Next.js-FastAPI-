import requests


def test_addTodo():
  url = "http://127.0.0.1:8000/todos"
  payload = {"title": "Test Todo"}
  response = requests.post(url, json=payload)
  assert response.status_code == 200


def test_getTodos():
  url = "http://127.0.0.1:8000/todos"
  response = requests.get(url)
  assert response.status_code == 200