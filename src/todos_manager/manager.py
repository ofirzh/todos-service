from typing import List


from src.todos_manager.schemas.todo import CreateTodo, Todo, UpdateTodo, UpdateTodoOrder
from motor import motor_asyncio
from bson import ObjectId


class TodosDBManager:
    def __init__(self, connection_str):
        self.client = motor_asyncio.AsyncIOMotorClient(connection_str)
        self.db = self.client.todosdb
        self.collection = self.client.todosdb["todos"]

    async def add(self, todo: CreateTodo) -> str:
        """
        Receives CreateTodo object and inserts into collection.
        :param todo:
        :return:
        """
        order = (await self.count()) * 100
        new_todo = await self.collection.insert_one({"title": todo.title, "order": order})
        return new_todo.inserted_id

    async def get(self, max_length=100, offset=0) -> List[Todo]:
        """
        Returns all todos.
        :return:
        """
        todos: List[Todo] = []
        cursor = self.collection.find()
        cursor.sort('order', 1).skip(offset).limit(max_length)
        for document in await cursor.to_list(length=max_length):
            todos.append(Todo(id=str(document["_id"]), title=document["title"]))
        return todos

    async def update(self, update: UpdateTodo) -> bool:
        """
        Receive update request and changes title of relevant todo
        :param update:
        """
        # find and replace title
        update_obj = {'title': update.title}
        result = await self.collection.update_one({'_id': ObjectId(update.id)}, {"$set": update_obj})
        return result.modified_count == 0

    async def update_order(self, update: UpdateTodoOrder) -> bool:
        """

        :param update:
        :return:
        """
        to_above_todo = await self.collection.find_one({'_id': ObjectId(update.above_id)})
        print(f"tobe above = {to_above_todo}")
        if to_above_todo is None:
            return False
        set_obj = {'order': to_above_todo["order"] - 1}
        result = await self.collection.update_one({'_id': ObjectId(update.id)}, {'$set': set_obj})
        return result.modified_count == 0

    async def count(self) -> int:
        """
        Returns todos count in collection
        :return:
        """
        return await self.collection.count_documents({})

    async def clear_all(self):
        """
        Clear this collection
        :return:
        """
        await self.collection.delete_many({})

