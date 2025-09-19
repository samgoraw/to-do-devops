# To-Do App (Python)

todos = []

def add_task(task):
    todos.append(task)
    return todos

def view_tasks():
    return todos

def delete_task(task_num):
    if 1 <= task_num <= len(todos):
        return todos.pop(task_num - 1)
    return None

# CLI only runs if executed directly
if __name__ == "__main__":
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            for i, t in enumerate(view_tasks(), start=1):
                print(f"{i}. {t}")
        elif choice == "3":
            num = int(input("Task number to delete: "))
            removed = delete_task(num)
            print(f"Removed: {removed}" if removed else "Invalid number")
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")
