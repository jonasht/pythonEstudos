from tkinter import *
from tkinter.messagebox import showerror
import shelve

# primeira vez usando shelve, entao estah em ingles 

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('people shelve')
    form = Frame(window)
    form.pack()
    entries ={}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    
    Button(window, text='fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='update', command=updateRecord).pack(side=LEFT)
    Button(window, text='quit', command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key].get()
    except:
        showerror(title='error', message='no such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from person import Person
        record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(entries[field].get()))
            db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()

    