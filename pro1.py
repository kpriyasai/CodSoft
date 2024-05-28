import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()