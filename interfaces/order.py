from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes.Item import *
from classes.Order import *


class OrderView:
    def __init__(self):
        self.window = Tk()
        self.window.title('Orders')
        self.window.geometry('503x500+0+0')

        self.item = Item()
        self.order = Order()

        self.all_items = self.item.show_item()
        self.ordered_item_list = []

        self.label_item = Label(self.window, text='Item')
        self.label_item.grid(row=0, column=0)

        self.combo_item = ttk.Combobox(self.window, state='readonly', width=27)
        self.combo_item.grid(row=0, column=1)
        # self.combo_item['values'] = self.all_items

        self.label_qty = Label(self.window, text='Qty')
        self.label_qty.grid(row=1, column=0)

        self.entry_qty = Entry(self.window, width=30)
        self.entry_qty.grid(row=1, column=1)

        self.btn_add_item = Button(self.window, text='Add >>', command=self.on_add_item)
        self.btn_add_item.grid(row=2, column=0)

        self.label_tbl = Label(self.window, text='Table No.')
        self.label_tbl.grid(row=3, column=0)

        self.entry_tbl = Entry(self.window, width=30)
        self.entry_tbl.grid(row=3, column=1)

        self.btn_add_order = Button(self.window, text='Submit Order', command=self.on_submit_order)
        self.btn_add_order.grid(row=4, column=0)

        self.btn_reset = Button(self.window, text='Reset', command=self.on_reset)
        self.btn_reset.grid(row=4, column=1)

        self.combo_order = ttk.Combobox(self.window)
        self.combo_order.grid(row=5, column=0)

        self.btn_show_order = Button(self.window, text='Show Order', command=self.show_orders_in_tree)
        self.btn_show_order.grid(row=5, column=1)

        self.order_tree = ttk.Treeview(self.window, column=('tbl', 'name', 'type', 'price', 'qty'))
        self.order_tree.grid(row=6, column=0, columnspan=2)
        self.order_tree['show'] = 'headings'
        self.order_tree.column('tbl', width=100, anchor='center')
        self.order_tree.column('name', width=100, anchor='center')
        self.order_tree.column('type', width=100, anchor='center')
        self.order_tree.column('price', width=100, anchor='center')
        self.order_tree.column('qty', width=100, anchor='center')
        self.order_tree.heading('tbl', text='Table No.')
        self.order_tree.heading('name', text='Name')
        self.order_tree.heading('type', text='Type')
        self.order_tree.heading('price', text='Price')
        self.order_tree.heading('qty', text='Qty')

        self.btn_bill = Button(self.window, text='Generate Bill', command=self.generate_bill)
        self.btn_bill.grid(row=7, column=0)

        self.show_items_in_combo()
        self.show_orders_in_combo()

        self.window.mainloop()

    def show_items_in_combo(self):
        show_items = []
        for i in self.all_items:
            show_items.append((i[1], i[2]))
        self.combo_item['values'] = show_items

    def on_add_item(self):
        # item_id = self.combo_item.get()[0]
        item_index = self.combo_item.current()
        # item_id = self.all_items[item_index][0]
        item = self.all_items[item_index]
        qty = self.entry_qty.get()
        self.ordered_item_list.append((item[0], qty))
        self.order_tree.insert('', 'end', text='', value=('', item[1], item[2], item[3], qty))

    def on_submit_order(self):
        if self.combo_order.get() == '':
            tbl = self.entry_tbl.get()
            if self.order.add_order(tbl, self.ordered_item_list):
                messagebox.showinfo('Order', 'Order added')
                self.show_orders_in_combo()
            else:
                messagebox.showerror('Error', 'Order can not added')
        else:
            order_id = self.combo_order.get()
            if self.order.add_order_to_prev_customer(self.ordered_item_list, order_id):
                messagebox.showinfo('Order', 'Order added')
                self.show_orders_in_combo()
            else:
                messagebox.showerror('Error', 'Order can not added')
        self.ordered_item_list.clear()

    def show_orders_in_combo(self):
        self.combo_order['values'] = self.order.show_all_orders()

    def show_orders_in_tree(self):
        order_id = self.combo_order.get()
        if order_id == '':
            messagebox.showerror('Error', 'Select Order number First')
        else:
            orders = self.order.show_orders_by_order_id(order_id)
            self.order_tree.delete(*self.order_tree.get_children())
            for i in orders:
                self.order_tree.insert('', 'end', text='', value=i)

    def on_reset(self):
        self.combo_order.set('')
        self.entry_qty.delete(0, END)
        self.entry_tbl.delete(0, END)
        self.order_tree.delete(*self.order_tree.get_children())
        self.ordered_item_list.clear()

    def generate_bill(self):
        if self.combo_order.get() == '':
            messagebox.showerror('Error', 'Select Order number First')
        else:
            orders = self.order_tree.get_children()
            if len(orders) == 0:
                messagebox.showerror('Error', 'Show order first')
            else:
                total = 0
                bill_list = []
                tbl_no = self.order_tree.item(orders[0], 'values')[0]
                for i in orders:
                    order = self.order_tree.item(i, 'values')
                    amt = float(order[3]) * float(order[4])
                    total += amt
                    bill_list.append((order[1], order[2], order[3], order[4], amt))
                    # tbl_no = order[0]
                BillView(bill_list, total, tbl_no)


class BillView:
    def __init__(self, bill_list, total, tbl):
        self.window = Tk()
        self.window.title('Bill')
        self.window.geometry('503x500+0+0')

        self.lbl_name = Label(self.window, text='Name: ').grid(row=0, column=0)
        self.lbl_namec = Label(self.window, text='').grid(row=0, column=1)

        self.lbl_tbl = Label(self.window, text='Table No.: ').grid(row=1, column=0)
        self.lbl_tblc = Label(self.window, text=tbl).grid(row=1, column=1)

        self.lbl_bill = Label(self.window, text='Bill By: ').grid(row=2, column=0)
        self.lbl_billby = Label(self.window, text='').grid(row=2, column=1)

        self.order_tree = ttk.Treeview(self.window, column=('name', 'type', 'price', 'qty', 'amt'))
        self.order_tree.grid(row=3, column=0, columnspan=2)
        self.order_tree['show'] = 'headings'
        self.order_tree.column('amt', width=100, anchor='center')
        self.order_tree.column('name', width=100, anchor='center')
        self.order_tree.column('type', width=100, anchor='center')
        self.order_tree.column('price', width=100, anchor='center')
        self.order_tree.column('qty', width=100, anchor='center')
        self.order_tree.heading('amt', text='Amount')
        self.order_tree.heading('name', text='Name')
        self.order_tree.heading('type', text='Type')
        self.order_tree.heading('price', text='Price')
        self.order_tree.heading('qty', text='Qty')

        for i in bill_list:
            self.order_tree.insert('', 'end', text='', values=i)

        self.order_tree.insert('', 'end', text='', values=('Total', '', '', '', total))

        self.window.mainloop()
