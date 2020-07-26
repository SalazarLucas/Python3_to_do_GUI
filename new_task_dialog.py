# Things to implement (User interface only):
# - Task input (Entry)
# - Date and Time inputs (Entries)
# - Combobox telling in what list the task will be added.
from mainwindow import *


# Widgets for the Top bar of the dialog
class GoBack(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='←', width=4)


class Title(Label):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='New Task')


class SaveTask(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='✔', width=4)


class DialogTopBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(2, weight=1)
        GoBack(self).grid(column=1, row=1)
        Title(self).grid(column=2, row=1)
        SaveTask(self).grid(column=3, row=1)


# Widgets for the dialog entry frame
class TaskEntry(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        Label(self, text='What is to be done?').grid(column=1, row=1, sticky=W)
        Entry(self).grid(column=1, row=2, sticky='nwse')


class Date(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        Label(self, text='Due date').grid(column=1, row=1, sticky=W)
        Entry(self).grid(column=1, row=2, sticky='nwse')


class TaskLists(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        Label(self, text='Add to List').grid(column=1, row=1, sticky=W)
        ListsCombobox(self).grid(column=1, row=2, sticky='nwse')


class DialogEntry(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        TaskEntry(self).grid(column=1, row=1, sticky='nwse')
        Date(self).grid(column=1, row=2, sticky='nwse')
        TaskLists(self).grid(column=1, row=3, sticky='nwse')


root = MainWindow()
DialogTopBar(root).grid(column=0, row=0, sticky='nwse')
DialogEntry(root).grid(column=0, row=1, sticky='nwse')
root.mainloop()
