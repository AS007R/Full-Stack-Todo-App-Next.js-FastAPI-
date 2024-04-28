from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from httpx._transports.wsgi import WSGITransport
from app.main import app, get_session, Todo
from app import settings



# Test with id available in db 
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

def test_delete_todo():
        todo_id = 111
        response = client.delete(f"/todos/{todo_id}")

        data = response.json()

        assert response.status_code == 200
        assert data["message"] == "Todo deleted"


# Test with id not available in db
def test_delete_todo_id_not_found():
        todo_id = 1
        response = client.delete(f"/todos/{todo_id}")

        data = response.json()

        assert response.status_code == 404
        assert data["detail"] == f"Todo with id {todo_id} not found."

      

  

 
