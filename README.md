# To do list using Python and Tkinter
## Libraries
- Tkinter
## GUI components
The application window (Tk) includes the following components:
- Entry Widget (e):
For the user to type tasks.
- Listbox Widget (l):
Displays the list of tasks.
- Buttons (b1, b2, b3):
Perform actions: Add, Delete, and Update tasks.
- Messages:
Uses tkinter.messagebox to show warnings when needed.
## Adding a Task
- Adds the entered text to the Listbox if it's not empty.
- Warns the user if no task is entered
```python
def add():
    t = e.get()  # Get the text from the Entry widget.
    if t:
        l.insert(END, t)  # Add it to the Listbox at the end.
        e.delete(0, END)  # Clear the Entry widget.
    else:
        showwarning("Warning", "Enter a task")
```
## Deleting a Task
- Deletes the selected task from the Listbox.
- Warns the user if no task is selected.
```python
def delete():
    try:
        idx = l.curselection()  # Get the selected item's index.
        l.delete(idx)  # Remove the selected item from the Listbox.
    except:
        showwarning("Warning", "Please select task to delete")
```
## Updating a Task
- Updates the selected task with new text entered in the Entry widget.
- Ensures that a task is selected and the new text is provided.
```python
def update():
    try:
        idx = l.curselection()  # Get the selected item's index.
        t = e.get()  # Get the updated task from the Entry widget.
        if t:
            l.delete(idx)  # Remove the old task.
            l.insert(idx, t)  # Insert the updated task at the same index.
            e.delete(0, END)  # Clear the Entry widget.
        else:
            showwarning("Warning", "Enter updated task")
    except:
        showwarning("Warning", "Select a task to update")
```
## Main Window
- Sets the title of the application as "To-Do list".
- Specifies a window size of 400x500 pixels.
- Colors the background red.
```python
w = Tk()
w.title("To-Do list")
w.geometry("400x500")
w.config(bg='red')
```
## Widget Packing
Each widget is placed vertically with padding:
```python
e.pack(padx=10, pady=10)   # Entry for input.
l.pack(padx=10, pady=10)   # Listbox for tasks.
b1.pack(padx=10, pady=10)  # Add Button.
b2.pack(padx=10, pady=10)  # Delete Button.
b3.pack(padx=10, pady=10)  # Update Button.
```
## Event Loop
Starts the application and keeps the window open to listen for user interactions.
```python 
w.mainloop()
```
