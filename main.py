from tkinter import *
from tkinter.messagebox import *
def add():
    t=e.get()
    if t:
        l.insert(END,t)
        e.delete(0,END)
    else:
        showwarning("Warning","Enter a task")
def delete():
    try:
        idx=l.curselection()
        l.delete(idx)
    except:
        showwarning("Warning","Please select task to delete")
def update():
    try:
        idx=l.curselection()
        t=e.get()
        if t:
            l.delete(idx)
            l.insert(idx,t)
            e.delete(0,END)
        else:
            showwarning("Warning","Enter updated task")
    except:
        showwarning("Warning","Select a task to update")
w=Tk()
w.title("To-Do list")
w.geometry("400x500")
w.config(bg='red')
e=Entry(w)
l=Listbox(w)
b1=Button(w,text="Add task",command=add)
b2=Button(w,text="Delete task",command=delete)
b3=Button(w,text="Update task",command=update)
e.pack(padx=10,pady=10)
l.pack(padx=10,pady=10)
b1.pack(padx=10,pady=10)
b2.pack(padx=10,pady=10)
b3.pack(padx=10,pady=10)
w.mainloop()