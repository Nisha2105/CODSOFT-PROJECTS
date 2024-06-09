from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Please enter a task.")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert(END, "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()

def delete():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No Tasks", "No tasks to delete.")
        return
    try:
        task_no = int(taskNumberField.get())
        if task_no < 1 or task_no > len(tasks_list):
            messagebox.showerror("Invalid Task Number", "Please enter a valid task number.")
            return
        tasks_list.pop(task_no - 1)
        counter -= 1
        clear_taskNumberField()
        TextArea.delete(1.0, END)
        for i in range(len(tasks_list)):
            TextArea.insert(END, "[ " + str(i + 1) + " ] " + tasks_list[i])
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid task number.")

# Create a GUI window
gui = Tk()
gui.configure(bg="black")
gui.title("ToDo App")
gui.geometry("300x400")

# Widgets
enterTask = Label(gui, text="Enter Your Task", bg="black", width=20, height=2, fg="white" ,font=("lucida calligraphy", 16))
enterTaskField = Entry(gui, width=30, font=("Arial", 12))
Submit = Button(gui, text="Add Task", fg="white", bg="green",width=10, height=1,font=("lucida calligraphy", 12), command=insertTask)
TextArea = Text(gui, height=10, width=30, font=("Arial", 12))
taskNumber = Label(gui, text="Delete Task Number", fg="white",font=("lucida calligraphy", 12), bg="black")
taskNumberField = Entry(gui, width=10, font=("lucida calligraphy", 12))
delete = Button(gui, text="Delete Task", fg="white", bg="red",width=10, height=1,font=("lucida calligraphy", 12), command=delete)
Exit = Button(gui, text="Exit", fg="white", bg="gray",width=10, height=1,font=("lucida calligraphy", 12), command=gui.quit)

# Grid Placement
enterTask.grid(row=0, column=0, padx=10, pady=(10, 5))
enterTaskField.grid(row=1, column=0, padx=10)
Submit.grid(row=2, column=0, padx=10, pady=5)
TextArea.grid(row=3, column=0, padx=10, pady=5)
taskNumber.grid(row=4, column=0, padx=10, pady=5)
taskNumberField.grid(row=5, column=0, padx=10)
delete.grid(row=6, column=0, padx=10, pady=5)
Exit.grid(row=7, column=0, padx=10, pady=(5, 10), sticky="we")

# Start the GUI
gui.mainloop()
