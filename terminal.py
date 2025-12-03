import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Your Tasks ---")
    for i, t in enumerate(tasks):
        status = "✔ Done" if t["completed"] else "❌ Pending"
        print(f"{i+1}. {t['task']} - {status}")
    print("------------------")

def mark_complete(tasks):
    view_tasks(tasks)
    if tasks:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1]["completed"] = True
        save_tasks(tasks)
        print("Task marked complete!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted!")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
