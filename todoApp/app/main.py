from typing import Optional, Annotated
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, SQLModel, Session, create_engine, select
from app import settings
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


#Creating SQLModel class for Todo model(table blue print) 
class Todo(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  title: str = Field(index=True)
  done: Optional[bool] = Field(default=False)

# create connection string from settings module 
connString:str = str(settings.BD_URL).replace(
  "postgresql", "postgresql+psycopg"
)

# create engine with connection string 
engine = create_engine(connString)

# create db and tables 
def create_db_and_tables():
  SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifeSpan(app: FastAPI):
  try:
    create_db_and_tables()
    yield
  finally:
    engine.dispose() # close connection 



# initialize app object from FastAPI class 
app = FastAPI(lifespan=lifeSpan, title="Todo App", version="0.0.1")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

def get_session():
  with Session(engine) as session:
    yield session

# define root route 
@app.get("/")
async def root():
  return {"message": "Hello World"}


# define route to get all todos 
@app.get("/todos")
async def get_todos(session: Annotated[Session, Depends(get_session)]):
  todos = session.exec(select(Todo)).all()
  return todos

#get todo by id
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
  todo = session.get(Todo, todo_id)
  if not todo:
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
  return todo

# define route to create todo
@app.post("/todos")
async def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
  if todo.title.strip():
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo
  else:
    raise HTTPException(status_code=400, detail="Title cannot be empty")

# define route to delete todo by id
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
  todo = session.get(Todo, todo_id)
  if not todo:
    return {"message": f"Todo with id {todo_id} not found"}
  
  session.delete(todo)
  session.commit()
  return {"message": "Todo deleted"}


# define route to update todo by id 
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
  todo_to_update = session.get(Todo, todo_id) 
  if not todo_to_update:
    return {"message": f"Todo with id {todo_id} not found"}
 
  if todo.title:
    if todo.title.strip():
      todo_to_update.title = todo.title
  if todo.done is not None:
    todo_to_update.done = todo.done
  
  session.commit()
  session.refresh(todo_to_update)
  return todo_to_update
  

