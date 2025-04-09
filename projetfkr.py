import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

# Function to delete the selected task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Delete task button
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()
