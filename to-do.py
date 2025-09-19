# Simple To-Do App (CLI)

todos = []

def show_menu():
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def save_task():
    task = input("Enter task: ")
    todos.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not todos:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if todos:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todos):
            removed = todos.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Choose option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
