from fastapi.testclient import TestClient
from sqlmodel import Field, Session, SQLModel, create_engine, select
from httpx._transports.wsgi import WSGITransport
from app.main import app, get_session, Todo
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
def test_update_todo():

    todo_id = 4
    todo_content = "Updated todo content"

    response = client.put(f"/todos/{todo_id}",
        json={"title": todo_content}
    )

    assert response.status_code == 200



def test_update_todo_not_found():
    todo_id = 1
    todo_content = "My test todo"

    response = client.put(f"/todos/{todo_id}",
        json={"title": todo_content}
    )

    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == f"Todo with id {todo_id} not found"

  


