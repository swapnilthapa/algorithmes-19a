from tkinter import *
from tkinter import messagebox
from classes.users import *
from interfaces.add_item import *


class LoginView:
    def __init__(self):
        self.window = Tk()
        self.window.title('Staff Login')
        self.window.geometry('300x300+0+0')

        self.user = Staff()

        self.lbl_un = Label(self.window, text="Username")
        self.lbl_un.grid(row=0, column=0)

        self.entry_un = Entry(self.window)
        self.entry_un.grid(row=0, column=1)

        self.lbl_pw = Label(self.window, text="Password")
        self.lbl_pw.grid(row=1, column=0)

        self.entry_pw = Entry(self.window, show='*')
        self.entry_pw.grid(row=1, column=1)

        self.btn_login = Button(self.window, text="Log In", command=self.do_login)
        self.btn_login.grid(row=3, column=0)

        self.window.mainloop()

    def do_login(self):
        self.user.set_un(self.entry_un.get())
        self.user.set_pw(self.entry_pw.get())
        data = self.user.login()
        if len(data) == 1:
            self.window.destroy()
            ItemView(data[0])
        else:
            messagebox.showerror('Error', 'Invalid login')


LoginView()
