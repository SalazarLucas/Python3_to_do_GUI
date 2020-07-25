# Things to implement:
# - Lists controller (combobox)
# - Search entry (Entry)
# - Button to add tasks in a list (it calls the new_task_dialog.py)
# - Entry to add quick tasks.
from tkinter import *
from tkinter import ttk


# Main Tk window
class MainWindow(Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('To do List')
        self.geometry('295x450')
        self.resizable(0, 0)
        # self.configure(background='#222222')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


class ListsCombobox(ttk.Combobox):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(state='readonly', values=None)


class AddTaskButton(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='+')


class QuickTaskEntry(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class SearchEntry(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class TaskGrid(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class TopBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        ListsCombobox(self).grid(column=0, row=0, sticky=W)
        SearchEntry(self).grid(column=1, row=0, sticky=E)


class BottomBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        QuickTaskEntry(self).grid(column=1, row=1)
        AddTaskButton(self).grid(column=2, row=1)


root = MainWindow()
TopBar(root).grid(column=0, row=0)
TaskGrid(root).grid(column=0, row=1, sticky='nwse')
BottomBar(root).grid(column=0, row=2)

root.mainloop()
