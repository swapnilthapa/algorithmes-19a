from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes.Item import Item
from interfaces.order import *


class ItemView:
    def __init__(self):
        self.window = Tk()
        self.window.title('Add Items')
        self.window.geometry('500x500+0+0')

        self.item = Item()
        # self.user = user

        self.update_index = ""

        self.item_name = Label(self.window, text="Item Name")
        self.item_name.grid(row=0, column=0)

        self.entry_name = Entry(self.window)
        self.entry_name.grid(row=0, column=1)

        self.item_type = Label(self.window, text="Item Type")
        self.item_type.grid(row=1, column=0)

        self.entry_type = Entry(self.window)
        self.entry_type.grid(row=1, column=1)

        self.item_rate = Label(self.window, text="Item Rate")
        self.item_rate.grid(row=2, column=0)

        self.entry_rate = Entry(self.window)
        self.entry_rate.grid(row=2, column=1)

        self.item_add = Button(self.window, text="Add Item", command=self.add_item)
        self.item_add.grid(row=3, column=0)

        self.item_update = Button(self.window, text="Update Item", command=self.update_item)
        self.item_update.grid(row=3, column=1)

        self.item_tree = ttk.Treeview(self.window, columns=('name', 'type', 'rate'))
        self.item_tree.grid(row=4, column=0, columnspan=2)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('name', width=100)
        self.item_tree.column('type', width=100)
        self.item_tree.column('rate', width=100)
        self.item_tree.heading('name', text="Name")
        self.item_tree.heading('type', text="Type")
        self.item_tree.heading('rate', text="Rate")

        self.item_type = Label(self.window, text="Welcome ")
        self.item_type.grid(row=5, column=0)

        self.show_item_tree()
        self.show_menu()

        self.window.mainloop()

    def add_item(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        rate = self.entry_rate.get()
        if self.validate():
            if self.item.add_item(name, type, rate):
                messagebox.showinfo('Item', "Item Added")
                self.show_item_tree()
            else:
                messagebox.showerror("Error", self.item.add_item(name, type, rate))

    def update_item(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            name = self.entry_name.get()
            type = self.entry_type.get()
            rate = self.entry_rate.get()
            if self.item.update_item(self.update_index, name, type, rate):
                messagebox.showinfo('Item', "Item Updated")
                self.show_item_tree()
                self.update_index = ""
            else:
                messagebox.showerror("Error", 'Can not be updated !!!')
      
    def show_item_tree(self):
        self.item_tree.delete(*self.item_tree.get_children())
        data = self.item.show_item()
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3]))
        self.item_tree.bind("<Double-1>", self.on_item_select)
      
    def on_item_select(self, event):
        selected_row = self.item_tree.selection()[0]
        selected_item = self.item_tree.item(selected_row, 'values')
        self.update_index = self.item_tree.item(selected_row, 'text')
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_item[0])
        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_item[1])
        self.entry_rate.delete(0, END)
        self.entry_rate.insert(0, selected_item[2])

    def open_order_window(self):
        OrderView()

    def show_menu(self):
        my_menu = Menu(self.window)
        self.window.config(menu=my_menu)
        order_menu = Menu(my_menu)
        my_menu.add_cascade(label="Order", menu=order_menu)

        order_menu.add_cascade(label="Add", command=self.open_add_order)
        order_menu.add_cascade(label="Show")
        order_menu.add_separator()
        order_menu.add_cascade(label="Exit", command=self.window.quit)

        bill_menu = Menu(my_menu)
        my_menu.add_cascade(label="Bill", menu=bill_menu)

        bill_menu.add_cascade(label="Generate")
        bill_menu.add_cascade(label="Show")

    def open_add_order(self):
        OrderView()

    def validate(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        rate = self.entry_rate.get()
        if name == '' or type == '' or rate == '':
            messagebox.showerror('Error', 'Fill all the fields')
            return False
        elif not rate.isdigit():
            messagebox.showerror('Error', 'Invalid value for rate')
            return False
        else:
            return True


