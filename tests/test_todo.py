import todo

def test_add_task():
    todo.todos.clear()
    todo.add_task("Buy milk")
    assert "Buy milk" in todo.view_tasks()

def test_delete_task():
    todo.todos.clear()
    todo.add_task("Task 1")
    todo.add_task("Task 2")
    removed = todo.delete_task(1)
    assert removed == "Task 1"
    assert "Task 1" not in todo.view_tasks()
