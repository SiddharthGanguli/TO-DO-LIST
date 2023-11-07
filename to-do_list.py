import tkinter as tk
from tkinter import messagebox

tasks = []

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_display()

# Function to remove a task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_display()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to display tasks
def update_display():
    task_listbox.delete(0, tk.END)
    i=1
    for task in tasks:
        task_listbox.insert(tk.END,task)
# Create the main window
root = tk.Tk()
root.title("To-Do List by Siddhartha Ganguli")
# root.attributes('-alpha',0.9)
root.minsize(490,300)
root.maxsize(490,350)

# Create the "Add Task" section
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

task_entry = tk.Entry(add_frame, width=40)
add_button = tk.Button(add_frame, text="Add Task", command=add_task)

task_entry.pack(side=tk.LEFT)
add_button.pack(side=tk.LEFT)

# Create the "Remove Task" section
remove_frame = tk.Frame(root)
remove_frame.pack()

remove_button = tk.Button(remove_frame, text="Remove Task", command=remove_task)
remove_button.pack()

# Create the "Display Task" section
display_frame = tk.Frame(root)
display_frame.pack()

task_listbox = tk.Listbox(display_frame, width=40)
task_listbox.pack()

# Create the "Quit" button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)




def delete_all_tasks():
    tasks.clear() 
    update_display()  

delete_all_button = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks)
delete_all_button.pack()

root.mainloop()
