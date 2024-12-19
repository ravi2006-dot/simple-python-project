import tkinter as tk
from tkinter import messagebox
import random

# Sample inspirational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "It always seems impossible until it's done.",
    "The future belongs to those who believe in the beauty of their dreams."
]

# Task Reminder App class
class TaskReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Reminder App")

        # Task list to store tasks
        self.tasks = []

        # Setting up the GUI
        self.task_label = tk.Label(root, text="Enter your task:")
        self.task_label.pack(pady=5)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            # Display a motivational quote when a task is marked as completed
            quote = random.choice(quotes)
            messagebox.showinfo("Motivation", f"Task completed! Here's a motivational quote:\n\n{quote}")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Setting up the main window
root = tk.Tk()
app = TaskReminderApp(root)
root.mainloop()
