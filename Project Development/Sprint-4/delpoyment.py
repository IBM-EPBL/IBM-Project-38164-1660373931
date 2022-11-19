import tkinter as tk
from tkinter import messagebox
# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import webbrowser
master=tkinter.Tk()



class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        border = tk.LabelFrame(self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=150)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)

        def register():
            window = tk.Tk()
            window.resizable(0, 0)

            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial", 15))
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15))
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15))
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x=235, y=110)

            l4 = tk.Label(window, text="Category", font=("Arial", 15))
            l4.place(x=80, y=220)

            Radiobutton(window, text="Farmer", padx=5, value=1).place(x=205, y=230)
            Radiobutton(window, text="others", padx=20,value=2).place(x=290, y=230)
            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "" :
                    if t2.get() == t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Sign in", font=("Arial", 15), command=check)
            b1.place(x=200, y=280)

            window.geometry("700x500")
            window.mainloop()

        B2 = tk.Button(self, text="Register", bg="dark orange", font=("Arial", 15), command=register)
        B2.place(x=650, y=20)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='Tomato')

        Label = tk.Label(self,
                         text="Store some content related to your \n project or what your application made for. \n All the best!!",
                         bg="orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)

class FourthPage(tk.Frame):
        def __init__(self, parent, controller):
             tk.Frame.__init__(self, parent)





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


class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# Imports
import tkinter
from tkinter import messagebox

# Message Box
messagebox.showinfo("Notification/Alert", "DETAILS ADDED")
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(800, 500)
app.mainloop()