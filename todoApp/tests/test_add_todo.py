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

def test_add_todo():


        response = client.post("/todos/",
            json={
                 "id": 111,
                 "title": "test todo title"}
        )

        data = response.json()

        assert response.status_code == 200
        assert data["title"] == "test todo title"
        assert data["id"] == 111


# Testing by passing todo without required feild.
def test_add_todo_required_feild_missing():
    response = client.post("/todos/",
        json={"id": 33}
    )
    data = response.json()

    assert response.status_code == 400
    assert data["detail"] == "Title cannot be empty"

# Testing without Optional feilds "id" and "done".
def test_add_todo_without_optional_feilds():
    response = client.post("/todos/",
        json={
              "title": "Testing todo without optional feilds 'id' and 'done'."
              }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Testing todo without optional feilds 'id' and 'done'."
        
  


 