from tkinter import *
import json


# Main Tk window
class MainWindow(Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('To do List')
        self.geometry('295x450')
        self.resizable(0, 0)
        self.configure(background='#222222')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


# Entry to add new tasks
class TaskEntry(Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(textvariable=task,
                       width=15,
                       background='#222222',
                       foreground='white',
                       highlightbackground='#222222',
                       insertbackground='white')
        self.grid(column=0, row=0, sticky='nwse')

    def delete_input(self):
        self.delete(0, 'end')


# Frame where the tasks will be displayed
class TaskFrame(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(background='#222222', padx=20)
        self.grid(column=0, row=1, sticky='nwse')
        self.grid_columnconfigure(0, weight=1)

    # Method to add tasks to the grid
    def add_task(self, *args):
        Task(self).grid(column=0, sticky='nswe')
        task_entry.delete_input()
        self.update_storage_file()

    # Method to check for stored tasks and add them to the grid
    def check_stored_tasks(self):
        try:
            with open('tasks.json', 'rt') as tasks:
                tasks_string_list = json.load(tasks)
            tasks.close()

            for string in tasks_string_list:
                if string != "":
                    task.set(string)
                    self.add_task()

        except FileNotFoundError:
            with open('tasks.json', 'wt') as tasks:
                json.dump([], tasks, indent=1)
            tasks.close()

    # Method to update the .json storage file
    def update_storage_file(self):
        with open('tasks.json', 'wt') as tasks:
            json.dump([w.checkbutton['text'] for w in self.winfo_children()], tasks, indent=1)
        tasks.close()


# Task that will be displayed in a TaskFrame instance
class Task(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Checkbutton to mark done tasks
        self.checkbutton = Checkbutton(self, text=task.get(), variable=self.info)
        self.checkbutton.configure(activebackground='#353535',
                                   activeforeground='#222222',
                                   background='#353535',
                                   foreground='#ffffff',
                                   highlightbackground='#353535',
                                   selectcolor='#353535',
                                   height=3)
        self.checkbutton.grid(column=1, row=1, sticky=W)

        # Button to close tasks
        self.button = Button(self, text='X', width=1, command=self.delete_task)
        self.button.configure(activebackground='#353535',
                              activeforeground='#222222',
                              bg='#353535',
                              fg='#ffffff',
                              highlightbackground='#353535',
                              relief='flat')
        self.button.grid(column=2, row=1)

        # Frame color
        self.configure(background='#353535',
                       highlightthickness=5,
                       highlightbackground='#222222')
        self.grid_columnconfigure(1, weight=1)

    def delete_task(self):
        self.grid_forget()
        self.destroy()
        task_frame.update_storage_file()


# Main window instantiation
root = MainWindow()

# String that will name tasks
task = StringVar()

# Entry and main application frame instantiation
task_entry = TaskEntry(root)
task_frame = TaskFrame(root)

task_entry.focus()
task_frame.check_stored_tasks()
root.bind('<Return>', task_frame.add_task)
root.mainloop()
