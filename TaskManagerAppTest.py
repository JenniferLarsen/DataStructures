import unittest
import tkinter as tk
from final_project_larsen import TaskManagerApp, Task, LinkedList


class TestTaskManagerApp(unittest.TestCase):
    def test_validate_input(self):
        app = TaskManagerApp(tk.Tk())
        self.assertTrue(app.validate_input("Description", "5", "2024-04-16"))
        self.assertFalse(app.validate_input("", "5", "2024-04-16"))
        self.assertFalse(app.validate_input("Description", "", "2024-04-16"))
        self.assertFalse(app.validate_input("Description", "abc", "2024-04-16"))

    def test_update_task_listbox(self):
        app = TaskManagerApp(tk.Tk())
        task1 = Task("Task 1", 1, "2024-04-16")
        task2 = Task("Task 2", 2, "2024-04-17")
        app.task_list = LinkedList()
        app.task_list.add_task(task1)
        app.task_list.add_task(task2)
        app.update_task_listbox()
        self.assertEqual(app.task_listbox.size(), 2)
        self.assertIn("Task 1", app.task_listbox.get(0))
        self.assertIn("Task 2", app.task_listbox.get(1))


if __name__ == "__main__":
    unittest.main()
