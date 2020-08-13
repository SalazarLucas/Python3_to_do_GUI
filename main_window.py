from tkinter import *
from tkinter.ttk import Scrollbar


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title('To do List')
        self.geometry('295x450')
        self.resizable(0, 0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class Task(Frame):
    """This class correspond to a Frame containing a checkbutton to mark
    the task as done."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.__checkbutton = Checkbutton(self, variable=self.info, command=lambda *args: self.__finish_task())
        self.__checkbutton.grid(sticky=W)

    @property
    def checkbutton(self):
        return self.__checkbutton

    @checkbutton.setter
    def checkbutton(self, text=None):
        self.__checkbutton.configure(text=text)

    def __finish_task(self):
        if self.__checkbutton['offvalue']:
            self.destroy()


class TaskGrid(Frame):
    """The tasks you have to finish will be displayed in a Frame inside this Frame."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Self configuration
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create a Canvas
        self.canvas = Canvas(self)
        self.canvas.grid(column=2, row=1, sticky='nwse')

        # Add a Scrollbar to the canvas
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(column=3, row=1, sticky='nwse')

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Create Another frame inside the canvas where the tasks will be displayed
        self.second_frame = Frame(self.canvas)

        # Add that new frame to a window in the canvas
        self.canvas.create_window((0, 0), window=self.second_frame, anchor='nw')


class QuickTaskEntry(Entry):
    """What to do? Type what you have to do in this entry and it will display your
    task on the task grid."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        default = 'Enter Quick Task Here'
        self.__quick_task_string = StringVar(value=default)
        self.configure(textvariable=self.__quick_task_string)
        self.bind('<FocusIn>', lambda *args: self.delete(0, END) if self.__quick_task_string.get() == default else None)
        self.bind('<FocusOut>', lambda *args: self.insert(0, default) if not self.__quick_task_string.get() else None)
        self.bind('<Return>', lambda *args: (display_task(), self.delete(0, END)))

    @property
    def quick_task_string(self):
        return self.__quick_task_string.get()


def display_task():
    """Function responsible to display tasks typed on the quick task entry on the task_grid instance."""
    if quick_task_entry.quick_task_string:
        new_quick_task = Task(task_grid.second_frame)
        new_quick_task.checkbutton = quick_task_entry.quick_task_string
        new_quick_task.grid(sticky=W)
        task_grid.canvas.configure(scrollregion=task_grid.canvas.bbox('all'))


root = Root()
task_grid = TaskGrid(root)
quick_task_entry = QuickTaskEntry(root)

task_grid.grid(column=0, row=0, columnspan=2, sticky='nwse')
quick_task_entry.grid(column=0, row=1, sticky='nwse')

root.mainloop()
