import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task."""
    task = simpledialog.askstring("Add Task", "Enter the new task:")
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        refresh_task_list()

def update_task():
    """Update a selected task."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Update Task", "No task selected.")
        return

    index = selected[0]
    task = tasks[index]

    def update_action():
        """Handle updating task actions."""
        action = update_var.get()
        if action == "Mark as Completed":
            task["completed"] = True
            save_tasks(tasks)
            refresh_task_list()
        elif action == "Edit Task":
            new_task = simpledialog.askstring("Edit Task", "Enter the updated task:", initialvalue=task["task"])
            if new_task:
                task["task"] = new_task
                save_tasks(tasks)
                refresh_task_list()
        update_window.destroy()

    update_window = tk.Toplevel(root)
    update_window.title("Update Task")
    update_var = tk.StringVar(value="Mark as Completed")
    
    tk.Radiobutton(update_window, text="Mark as Completed", variable=update_var, value="Mark as Completed").pack(anchor=tk.W)
    tk.Radiobutton(update_window, text="Edit Task", variable=update_var, value="Edit Task").pack(anchor=tk.W)
    tk.Button(update_window, text="Update", command=update_action).pack()

def delete_task():
    """Delete the selected task."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Delete Task", "No task selected.")
        return

    index = selected[0]
    deleted_task = tasks.pop(index)
    save_tasks(tasks)
    refresh_task_list()
    messagebox.showinfo("Task Deleted", f"Deleted task: {deleted_task['task']}")

def refresh_task_list():
    """Refresh the task list display."""
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        task_listbox.insert(tk.END, f"{index + 1}. [{status}] {task['task']}")

# GUI setup
root = tk.Tk()
root.title("To-Do List Application")

# Load tasks
tasks = load_tasks()

# Task list display
task_frame = tk.Frame(root)
task_frame.pack(padx=10, pady=10)

task_listbox = tk.Listbox(task_frame, width=50, height=15)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_frame, orient="vertical")
scrollbar.config(command=task_listbox.yview)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Task", width=15, command=update_task)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5)

# Initialize task list
refresh_task_list()

# Run the application
root.mainloop()
