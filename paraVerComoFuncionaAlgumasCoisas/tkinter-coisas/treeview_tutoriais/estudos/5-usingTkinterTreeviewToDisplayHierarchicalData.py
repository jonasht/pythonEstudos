# Using Tkinter Treeview to display hierarchical data


import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from tkinter.messagebox import showinfo

# create root window
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading('text', text='Departments', anchor='w')


# adding data
tree.insert('', END, text='Administration', iid=0, open=False)
tree.insert('', END, text='Logistics', iid=1, open=False)
tree.insert('', END, text='Sales', iid=2, open=False)
tree.insert('', END, text='Finance', iid=3, open=False)
tree.insert('', END, text='IT', iid=4, open=False)

# adding children of first node
tree.insert('', END, text='John Doe', iid=5, open=False)
tree.insert('', END, text='Jane Doe', iid=6, open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()