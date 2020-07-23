# users - properties/attributes(variables) and behaviour/features(methods)
from classes.connection import *


class Staff:
    _username = ""
    _password = ""
    # _name = ""
    # _address = ""
    # _email = ""
    # _phone = ""
    # _type = ""

    def __init__(self):
        # self._username = un
        # self._password = pw
        self.db = MyDb()

    def set_un(self, un):
        # if not un.isalphnum():
        #     return False
        self._username = un

    def get_un(self):
        return self._username

    def set_pw(self, pw):
        self._password = pw

    def get_pw(self):
        return self._password

    def login(self):
        # self._username = un
        # self._password = pw
        qry = "SELECT * FROM users WHERE username = %s and password = %s"
        values = (self._username, self._password)
        # values = (un, pw)
        user = self.db.show_data_p(qry, values)
        return user


class Admin(Staff):
    def __init__(self):
        pass

    def register(self):
        qry = """INSERT INTO users (username, password, name, address, email, phone, type) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""

