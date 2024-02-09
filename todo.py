import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Create task entry
        self.task_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
        self.task_entry.pack(pady=(20, 10))

        # Create add button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="lightblue")
        self.add_button.pack(pady=5)

        # Create listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, width=50, font=("Helvetica", 12), selectbackground="lightblue", selectforeground="black")
        self.tasks_listbox.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Create buttons for marking as completed and deleting tasks
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed, font=("Helvetica", 12), bg="lightgreen")
        self.complete_button.pack(side=tk.LEFT, padx=(20, 5), pady=5, anchor="w")
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), bg="salmon")
        self.delete_button.pack(side=tk.RIGHT, padx=(5, 20), pady=5, anchor="e")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def mark_as_completed(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.itemconfig(selected_index, bg="lightgreen")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def delete_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.geometry("400x300")  # Initial size
    root.resizable(True, True)  # Allow resizing in both directions
    root.mainloop()

if __name__ == "__main__":
    main()
