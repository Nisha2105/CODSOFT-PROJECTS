from tkinter import *
import random
import pyperclip

tk=Tk()
tk.geometry('300x300')
tk.configure(background='light green')

pswd=StringVar()
passlen=IntVar()
passlen.set('')

def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    password=''
    if passlen.get()>=4:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)

def copyclipboard():
    random_password = pswd.get()
    pyperclip.copy(random_password)
    Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)

Label(tk, text="Strong Password Generator", font="Courier 12 bold",bg='green',fg='white').pack()
Label(tk, text="Enter your desired  length of password\n(Minimum length should be 4)",font="Courier 8 bold",bg='green',fg='white').pack(pady=3)
Entry(tk, textvariable=passlen).pack(pady=6)
Button(tk, text="Generate Password", command=password_generator,bg='light blue',fg='black').pack(pady=7)
Entry(tk, textvariable=pswd).pack(pady=6)
Button(tk, text="Copy to clipboard", command=copyclipboard,bg='light blue',fg='black').pack()

# To initiate and display the root window we created
tk.mainloop()