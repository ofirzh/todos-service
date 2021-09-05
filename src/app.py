from os import environ as env
from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException
from src.utils.logger import init_logging
from src.todos_manager.manager import TodosDBManager
from src.todos_manager.schemas.todo import CreateTodo, Todo, UpdateTodo, UpdateTodoOrder

# Load configurations
HOST = env.get('APP_HOST', "0.0.0.0")
PORT = int(env.get('APP_PORT', 8080))
LOG_LEVEL = env.get('LOGLEVEL', 'DEBUG').upper()
DB_URL = env.get('DB_URL', 'mongodb://localhost:27017')


# Initialize TodosDbManger and web service
todos_db_manager = TodosDBManager(DB_URL)
app = FastAPI()
logger = init_logging(LOG_LEVEL)


@app.post("/todos", response_model=Todo, status_code=201)
async def add_todo(todo: CreateTodo) -> Todo:
    logger.debug(f"Create todo request: {todo}")
    new_id = await todos_db_manager.add(todo)
    return Todo(id=str(new_id), title=todo.title, done=False)


@app.get("/todos",  response_model=List[Todo])
async def get_todos() -> List[Todo]:
    logger.debug(f"get todos request")
    todos = await todos_db_manager.get()
    return todos


@app.put("/todos", status_code=200)
async def update_todo(todo: UpdateTodo):
    logger.debug(f"Update todo request: {todo}")
    res = await todos_db_manager.update(todo)
    if not res:
        raise HTTPException(status_code=404, detail="not found")
    return {}


@app.patch("/todos", status_code=200)
async def update_todo_order(todo: UpdateTodoOrder):
    logger.debug(f"Update order of todo request: {todo}")
    res = await todos_db_manager.update_order(todo)
    if not res:
        raise HTTPException(status_code=404, detail="not found")
    return {}


@app.get("/clear_all", status_code=200)
async def clear_todos():
    logger.debug(f"Clear all todos request")
    await todos_db_manager.clear_all()
    return {}

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT)
