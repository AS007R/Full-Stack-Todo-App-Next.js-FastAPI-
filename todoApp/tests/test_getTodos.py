import requests

def test_getTodos():
  url = "http://127.0.0.1:8000/todos"
  response = requests.get(url)
  assert response.status_code == 200