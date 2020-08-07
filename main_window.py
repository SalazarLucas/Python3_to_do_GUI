from tkinter import *
from tkinter.ttk import *


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title('To do List')
        self.geometry('295x450')
        self.resizable(0, 0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class Task(Frame):
    """This class correspond to a Frame containing a checkbutton to mark
    the task as done."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.__checkbutton = Checkbutton(self, variable=self.info)
        self.__checkbutton.grid(sticky=W)

    @property
    def checkbutton(self):
        return self.__checkbutton

    @checkbutton.setter
    def checkbutton(self, text=None):
        self.__checkbutton.configure(text=text)


class Lists(Combobox):
    """This is a ttk Combobox with the lists, so you can split your tasks per subject."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(state='readonly', values=['Teste1', 'Teste2', 'Teste3'])


class TaskGrid(Frame):
    """The tasks you have to finish will be displayed in this Frame."""
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


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
    new_quick_task = Task(task_grid)
    new_quick_task.checkbutton = quick_task_entry.quick_task_string
    new_quick_task.grid(sticky=W)


root = Root()
lists = Lists(root)
task_grid = TaskGrid(root)
quick_task_entry = QuickTaskEntry(root)

lists.grid(column=0, row=0, sticky='nwse')
task_grid.grid(column=0, row=1, columnspan=2, sticky='nwse')
quick_task_entry.grid(column=0, row=2, sticky='nwse')

root.mainloop()
