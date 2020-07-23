import mysql.connector

# establishes connection
# executes query
# return data after query execution if necessary
# can be used for any tables providing values to parameters asked


class MyDb:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="",
                             host="localhost", port=3306, database='es19a') #to access databse
        self.my_cursor = self.my_connection.cursor() #to execute query

    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            return False

    def insert_with_id_return(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def show_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    def show_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data













# d = MyDb()
# print(d.my_connection)


# qry = "CREATE DATABASE es19a"
# qry = "CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, name varchar(100), type varchar(100), price double)"
# qry = "INSERT INTO items (name, type, price) VALUES (%s,%s,%s)"
# values = ('Pizza', 'Chicken', 100)
# my_cursor.execute(qry, values)
# my_connection.commit()

# qry = "SELECT * FROM items"
# my_cursor.execute(qry)
# all_items = my_cursor.fetchall()
# for i in all_items:
#     print(i[0], i[1], i[2], i[3])


# class Student:
#     def __init__(self):
#         pass
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_address(self):
#         return self.__address
#
#     def set_address(self, add):
#         self.__address = add
#
#     def set_age(self, age):
#         if int(age) > 25:
#             print("Not eligible")
#         self.__age = age
#
#
# name = input("Enter you name")
# add = input("Enter you address")
# age = input("Enter you age")
#
# s = Student()
# s.set_age(age)
# s.set_name(name)
# s.set_address(add)
#
# print(s.get_name())
# print(s.get_address())


# features
# encapsulation
# inheritance
# polymorphism
# abstraction