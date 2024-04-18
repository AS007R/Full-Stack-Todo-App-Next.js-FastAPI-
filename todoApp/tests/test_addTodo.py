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
                 "id": 34,
                 "title": "test todo title"}
        )

        data = response.json()

        assert response.status_code == 200
        assert data["title"] == "test todo title"
        assert data["id"] == 34


# def test_add_todo1():


#         response = client.post("/todos/",
#             json={
#                  "id": 33,
#                  "title": "test todo title",}
#         )

#         data = response.json()

#         assert response.status_code == 422
        
  


