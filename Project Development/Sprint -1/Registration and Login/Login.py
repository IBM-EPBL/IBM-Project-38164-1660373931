from tkinter import *
from functools import partial
import sqlite3
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
def database():
    name = username.get()
    pswd=password.get()

    conn = sqlite3.connect('login.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS VIEWER (name TEXT,password TEXT)')
    cursor.execute('INSERT INTO VIEWER (name,password) VALUES(?,?)',(name,password))
    conn.commit()
#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()