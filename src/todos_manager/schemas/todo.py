from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    id: str


class CreateTodo(BaseModel):
    title: str


class UpdateTodo(BaseModel):
    id: str
    title: str


class UpdateTodoOrder(BaseModel):
    id: str
    above_id: str
