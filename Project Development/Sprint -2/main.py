# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import webbrowser
master=tkinter.Tk()


# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg():

   import tkinter as tk
   root = Tk()
   root.title = 'link to the button'




   def link():
      webbrowser.open_new("file:///C:/Users/dell/Downloads/Estimation%20of%20crop%20yield.html")

   nut = ttk.Button(root, text='Crops and details',command=link)

   nut.pack()
   root.mainloop()
   root.update()

# Add an optional Label widget
Label(win, text= "Welcome !", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "view", command=show_msg).pack(pady= 20)
win.mainloop()

