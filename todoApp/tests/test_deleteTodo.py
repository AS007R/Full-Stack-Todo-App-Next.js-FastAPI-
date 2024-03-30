import requests


def test_deleteTodo():
  url = "http://127.0.0.1:8000/todos/10"
  response = requests.delete(url)
  assert response.status_code == 200

def test_deleteTodo2():
  url = "http://127.0.0.1:8000/todos/11"
  response = requests.delete(url)
  assert response.status_code == 200