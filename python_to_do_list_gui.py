from tkinter import *


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

        # Entry to receive new tasks from user
        self['textvariable'] = task
        self['width'] = 15
        self.configure(background='#222222',
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

        # Frame configuration
        self.configure(background='#222222', padx=20)
        self.grid(column=0, row=1, sticky='nwse')
        self.grid_columnconfigure(0, weight=1)


# Task that will be displayed in a TaskFrame instance
class Task(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Checkbutton to mark done tasks
        self.checkbutton = Checkbutton(self, variable=self.info)
        self.checkbutton.configure(background='#222222',
                                   foreground='white',
                                   highlightbackground='#222222',
                                   selectcolor='#222222')
        self.checkbutton.grid(column=1, row=1)

        # Label with the task to be done
        self.label = Label(self, text=task.get())
        self.label.configure(background='#222222',
                             foreground='white', height=4,
                             anchor=W)
        self.label.grid(column=2, row=1, sticky='nwse')

        # Button to close tasks
        self.button = Button(self, text='X', width=1, command=self.delete_task)
        self.button.configure(bg='#222222',
                              fg='white',
                              highlightbackground='#222222',
                              relief='flat')
        self.button.grid(column=3, row=1)

        # Frame color
        self.configure(background='#222222')
        self.grid_columnconfigure(2, weight=1)

    def delete_task(self):
        self.grid_forget()
        self.destroy()

    @staticmethod
    def add_task(*args):
        Task(task_frame).grid(column=0, sticky='nswe')
        task_entry.delete_input()


root = MainWindow()

task = StringVar()

task_entry = TaskEntry(root)
task_frame = TaskFrame(root)

task_entry.focus()
root.bind('<Return>', Task.add_task)
root.mainloop()
