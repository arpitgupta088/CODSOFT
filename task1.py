import json
import os

TODO_FILE = "to_do_list.arpit"

def task_load():
    """Load tasks from a file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def task_save(tasks):
    """Save tasks to a file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def task_add(tasks):
    """Add a new task."""
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    task_save(tasks)
    print("Task added successfully!")

def task_view(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    
    for ind, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{ind}. [{status}] {task['task']}")

def task_update(tasks):
    """Update a task."""
    task_view(tasks)
    try:
        task_num = int(input("Enter the number of task you want to update: ")) - 1
        if 0 <= task_num < len(tasks):
            task = tasks[task_num]
            print(f"Selected task: {task['task']}")
            want = input("Mark as completed (c) / Edit (e): ").lower()
            
            if want == 'c':
                task["completed"] = True
                print("Task marked as completed.")
            elif want == 'e':
                new_task = input("Enter the updated task: ")
                task["task"] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid action.")
        else:
            print("Task number is not valid.")
    except ValueError:
        print("Please enter a valid number.")
    
    task_save(tasks)

def task_delete(tasks):
    """Delete a task."""
    task_view(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
    task_save(tasks)

def main():
    """Main function to run the To-Do list application."""
    tasks = task_load()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice from (1-5): ")
        
        if choice == '1':
            task_add(tasks)
        elif choice == '2':
            task_view(tasks)
        elif choice == '3':
            task_update(tasks)
        elif choice == '4':
            task_delete(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice!! Please enter a number between 1 & 5 ")

if __name__ == "__main__":
    main()
