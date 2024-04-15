"""
/***************************************************************
    * Name : final_project_larsen.py
    * Author: Jennifer Larsen
    * Created : 4/15/2024
    * Course: CIS 152 - Data Structure
    * Version: 1.0
    * OS: Windows 11
    * IDE: PyCharm 2022.3.2
    * Copyright : This is my own original work
    * based on specifications issued by our instructor
    * Description : An app that illustrates heaps.
    * Input: An array of numbers for a heap
    * Output: the heap
    * BigO: [TODO]
    * Academic Honesty: I attest that this is my original work.
    * I have not used unauthorized source code, either modified or
    * unmodified. I have not given other fellow student(s) access
    * to my program.
    ***************************************************************
"""

import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date


class LinkedListNode:
    def __init__(self, task):
        self.task = task
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = LinkedListNode(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.priority < pivot.priority]
    middle = [x for x in arr if x.priority == pivot.priority]
    right = [x for x in arr if x.priority > pivot.priority]
    return quicksort(left) + middle + quicksort(right)


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management Application")
        self.task_list = LinkedList()
        self.create_widgets()

    def create_widgets(self):
        self.description_label = tk.Label(self.root, text="Task Description:")
        self.description_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.priority_label = tk.Label(self.root, text="Task Priority:")
        self.priority_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.priority_entry = tk.Entry(self.root)
        self.priority_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.due_date_label = tk.Label(self.root, text="Due Date:")
        self.due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.handle_add_task)
        self.add_task_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    def validate_input(self, description, priority, due_date):
        if not description or not priority or not due_date:
            return False
        return True

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        current = self.task_list.head
        while current:
            task_str = f"{current.task.description} - Priority: {current.task.priority} - Due Date: {current.task.due_date}"
            self.task_listbox.insert(tk.END, task_str)
            current = current.next

    def handle_add_task(self):
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()
        if self.validate_input(description, priority, due_date):
            task = Task(description, int(priority), due_date)
            self.task_list.add_task(task)
            self.update_task_listbox()
            messagebox.showinfo("Success", "Task added successfully!")
            self.description_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)


root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
