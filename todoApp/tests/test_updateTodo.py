import requests


# testing update todo request

def test_updateTodo():
  url = "http://127.0.0.1:8000/todos/7"
  payload = {"done": True}
  response = requests.put(url, json=payload)
  assert response.status_code == 200

def test_getTodos():
  url = "http://127.0.0.1:8000/todos"
  response = requests.get(url)
  assert response.status_code == 200