# Things to implement (User interface only):
# - Lists controller (combobox)
# - Search entry (Entry)
# - Button to add tasks in a list (it calls the new_task_dialog.py)
# - Entry to add quick tasks.
from tkinter import *
from tkinter import ttk
from new_task_dialog import DialogMainFrame


# Main Tk window
class MainWindow(Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('To do List')
        self.geometry('295x450')
        self.resizable(0, 0)
        # self.configure(background='#222222')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def call_new_task_dialog(self):
        DialogMainFrame(self).grid(column=0, row=0, sticky='nwse')


class ListsCombobox(ttk.Combobox):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(state='readonly', values=None)


class NewTaskButton(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='+', command=root.call_new_task_dialog)


class QuickTask(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class Search(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class TaskGrid(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class TopBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        ListsCombobox(self).grid(column=0, row=0, sticky=W)
        Search(self).grid(column=1, row=0, sticky=E)


class BottomBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        QuickTask(self).grid(column=1, row=1, sticky='nwse')
        NewTaskButton(self).grid(column=2, row=1)


# Frame containing TopBar, BottomBar and TaskGrid
class MainWindowMainframe(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        TopBar(self).grid(column=1, row=1, sticky='nwse')
        TaskGrid(self).grid(column=1, row=2, sticky='nwse')
        BottomBar(self).grid(column=1, row=3, sticky='nwse')


root = MainWindow()
MainWindowMainframe(root).grid(column=0, row=0, sticky='nwse')
root.mainloop()
