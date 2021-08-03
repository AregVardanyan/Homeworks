import sqlite3
from sqlite3 import Error
import os
import sys

print(os.getcwd())
try:
    os.mkdir(os.path.join(os.getcwd(), 'databases'))
except FileExistsError:
    pass


class Book(object):
    def __init__(self, name, author, publish_date, rate):
        self.Name = name
        self.Author = author
        self.Date = publish_date
        self.Rate = rate
        self.status = False
        self.conn = None
        self.curs = None
        self.table_name = None

    def connect_to_db(self, directory):
        database = directory
        try:
            self.conn = sqlite3.connect(database)
            self.curs = self.conn.cursor()
            self.table_name = directory.split('\\')[-1].split('/')[-1].split('.')[0]
            book_query = f""" CREATE TABLE IF NOT EXISTS {self.table_name} (
                                                     id integer PRIMARY KEY,
                                                     Name text NOT NULL,
                                                     Author text,
                                                     Date text,
                                                     Rate integer
                                             ); """
            self.curs.execute(book_query)
            self.conn.commit()
            self.status = True
        except Error:
            print(Error)
            sys.exit()

    def add_book(self):
        if self.status:
            if not(self.Name in self.list_books()):
                update_query = f"""INSERT INTO {self.table_name} (Name, Author, Date, Rate)
                                         VALUES('{self.Name}', '{self.Author}', '{self.Date}', '{self.Rate}'); """
                self.curs.execute(update_query)
                self.conn.commit()
        else:
            raise Exception("Ypu must connect to the db")

    def del_book(self):
        if self.status:
            del_query = f"""DELETE FROM {self.table_name}
                                     WHERE name = '{self.Name}'; """
            self.curs.execute(del_query)
            self.conn.commit()
        else:
            raise Exception("Ypu must connect to the db")

    def list_books(self):
        if self.status:
            self.curs.execute(f"SELECT Name FROM {self.table_name}")
            book_list = self.curs.fetchall()
            book_list = [i[0] for i in book_list]
            return book_list


book1 = Book("Tom Sawyer", "Mark Twain", "1876", 4)
directory1 = os.path.join(os.getcwd(), 'databases', 'books.db')
book1.connect_to_db(directory1)
book1.add_book()
book1.list_books()
book2 = Book("Samvel", "Raffi", "1886", 5)
book2.connect_to_db(directory1)
book2.add_book()
