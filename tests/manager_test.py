import asyncio
from src.todos_manager.schemas.todo import CreateTodo, Todo, UpdateTodo, UpdateTodoOrder
from src.todos_manager.manager import TodosDBManager


async def main():
    url = 'mongodb://localhost:27017'
    tm = TodosDBManager(url)
    await tm.clear_all()
    count = await tm.count()
    print(f"count: {count}")
    t1 = CreateTodo(title="first")
    await tm.add(t1)
    t2 = CreateTodo(title="second")
    await tm.add(t2)
    t3 = CreateTodo(title="third")
    await tm.add(t3)

    list = await tm.get()
    print(list)
    assert list[0].title == "first"
    assert list[1].title == "second"
    assert await tm.count() == 3

    print("test ADD passed")
    up1 = UpdateTodo(id=list[0].id, title="first1")
    await tm.update(up1)
    list = await tm.get()
    print(list)
    assert list[0].title == "first1"
    print("test UPDATE passed")

    up_order = UpdateTodoOrder(id=list[2].id, above_id=list[0].id)
    await tm.update_order(up_order)
    list = await tm.get()
    print("after reorder")
    print(list)
    assert list[0].title == "third"

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
