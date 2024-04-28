from fastapi.testclient import TestClient
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.main import app, get_session
from app import settings



connection_string = str(settings.TEST_DB_URL).replace(
"postgresql", "postgresql+psycopg")

engine = create_engine(
    connection_string)

SQLModel.metadata.create_all(engine)  

with Session(engine) as session:  

    def get_session_override():  
            return session  

    app.dependency_overrides[get_session] = get_session_override 

    client = TestClient(app=app)

def test_get_todo_by_id():
    todo_id = 8
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200

# Testing with id not in db
def test_get_todo_by_id_not_found():
    todo_id = 100
    response = client.get(f"/todos/{todo_id}")
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == f"Todo with id {todo_id} not found"

  
