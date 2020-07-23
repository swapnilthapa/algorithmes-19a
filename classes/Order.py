from classes.connection import MyDb


class Order:
    def __init__(self):
        self.my_db = MyDb()

    def add_order(self, tbl, ordered_items_list):
        #orders -> tbl_no
        qry = "INSERT INTO orders (tbl_no) VALUES (%s)"
        values = (tbl,)
        order_id = self.my_db.insert_with_id_return(qry, values)
        # ordered_items -> item_id, qty, order_id
        # ordered_items_list = [(1,2), (2,3), (7,2)]
        for i in ordered_items_list:
            qry = "INSERT INTO ordered_items (item_id, qty, order_id) VALUES (%s, %s, %s)"
            values = (i[0], i[1], order_id)
            self.my_db.iud(qry, values)
        return True

    def add_order_to_prev_customer(self, ordered_items_list, order_id):
        for i in ordered_items_list:
            qry = "INSERT INTO ordered_items (item_id, qty, order_id) VALUES (%s, %s, %s)"
            values = (i[0], i[1], order_id)
            self.my_db.iud(qry, values)
        return True

    def show_orders_by_order_id(self, order_id): #order_id as customer no.
        qry = """ SELECT orders.tbl_no, items.name, items.type, items.price, ordered_items.qty FROM ordered_items 
                    JOIN items ON ordered_items.item_id = items.id
                    JOIN orders ON ordered_items.order_id = orders.id
                    WHERE ordered_items.order_id = %s """
        val = (order_id,)
        all_orders = self.my_db.show_data_p(qry, val)
        return all_orders

    def show_all_orders(self):
        qry = "SELECT id FROM orders"
        orders = self.my_db.show_data(qry)
        return orders

    def cancel_order(self):
        pass

    def show_complementary_item(self):
        pass
