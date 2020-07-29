# Things to implement (User interface only):
# - Lists controller (combobox)
# - Search entry (Entry)
# - Button to add tasks in a list (it calls the new_task_dialog.py)
# - Entry to add quick tasks.
from tkinter import *
from tkinter import ttk
from new_task_dialog import DialogMainFrame, TaskWidget


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
        dialog = DialogMainFrame(self)
        dialog.grid(column=0, row=0, sticky='nwse')


class ListsCombobox(ttk.Combobox):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(state='readonly', values=None)


class Search(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class NewTaskButton(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(text='+', command=root.call_new_task_dialog)


class QuickTask(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.task_string = StringVar(value='Enter Quick Task Here')
        self.configure(textvariable=self.task_string)

        self.bind('<FocusIn>', lambda *args: self.delete(0, END))
        self.bind('<FocusOut>', lambda *args: self.insert(0, 'Enter Quick Task Here'))


class TaskGrid(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)


class TopBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.lists_combobox = ListsCombobox(self)
        self.search = Search(self)

        self.lists_combobox.grid(column=0, row=0, sticky=W)
        self.search.grid(column=1, row=0, sticky=E)


class BottomBar(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_columnconfigure(1, weight=1)
        self.quick_task_entry = QuickTask(self)
        self.new_task_button = NewTaskButton(self)

        self.quick_task_entry.grid(column=1, row=1, sticky='nwse')
        self.new_task_button.grid(column=2, row=1)


# Frame containing TopBar, BottomBar and TaskGrid
class MainWindowMainframe(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.top_bar = TopBar(self)
        self.task_grid = TaskGrid(self)
        self.bottom_bar = BottomBar(self)

        self.top_bar.grid(column=1, row=1, sticky='nwse')
        self.task_grid.grid(column=1, row=2, sticky='nwse')
        self.bottom_bar.grid(column=1, row=3, sticky='nwse')


def add_quick_task(*args):
    TaskWidget(mainframe.task_grid, mainframe.bottom_bar.quick_task_entry.task_string.get()).grid(sticky='nwse')
    mainframe.task_grid, mainframe.bottom_bar.quick_task_entry.delete(0, END)


root = MainWindow()

mainframe = MainWindowMainframe(root)
mainframe.grid(column=0, row=0, sticky='nwse')
mainframe.bottom_bar.quick_task_entry.bind('<Return>', add_quick_task)

root.mainloop()
