# Things to implement (User interface only):
# - Task input (Entry)
# - Date and Time inputs (Entries)
# - Combobox telling in what list the task will be added.
from tkinter import *
from tkinter.ttk import Combobox


# Widgets for the Top bar of the dialog
class GoBack(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='←', width=4, command=self.master.master.destroy)


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

        self.go_back = GoBack(self)
        self.title = Title(self)
        self.save_task = SaveTask(self)

        self.go_back.grid(column=1, row=1)
        self.title.grid(column=2, row=1)
        self.save_task.grid(column=3, row=1)


# Widgets for the dialog entry frame
class TaskEntry(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)

        self.new_task_string = StringVar()

        self.label = Label(self, text='What is to be done?')
        self.entry = Entry(self, textvariable=self.new_task_string)

        self.label.grid(column=1, row=1, sticky=W)
        self.entry.grid(column=1, row=2, sticky='nwse')


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
        Combobox(self).grid(column=1, row=2, sticky='nwse')


class DialogEntry(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)

        self.task_entry = TaskEntry(self).grid(column=1, row=1, sticky='nwse')
        self.date = Date(self).grid(column=1, row=2, sticky='nwse')
        self.task_lists = TaskLists(self).grid(column=1, row=3, sticky='nwse')


class DialogMainFrame(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)

        self.dialog_top_bar = DialogTopBar(self)
        self.dialog_entry = DialogEntry(self)

        self.dialog_top_bar.grid(column=1, row=1, sticky='nwse')
        self.dialog_entry.grid(column=1, row=2, sticky='nwse')


class TaskWidget(Frame):
    def __init__(self, master, txt, **kw):
        super().__init__(master, **kw)
        Checkbutton(self, text=txt, variable=self.info).grid(column=1, row=1, sticky=W)


