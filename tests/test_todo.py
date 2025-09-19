# tests/test_todo.py
import sys
import os

# make repo root importable (so pytest can find todo.py at project root)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
