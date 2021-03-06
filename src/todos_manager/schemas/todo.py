from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    id: str
    done: bool


class CreateTodo(BaseModel):
    title: str


class UpdateTodo(BaseModel):
    id: str
    title: str
    done: bool


class UpdateTodoOrder(BaseModel):
    id: str
    above_id: str
