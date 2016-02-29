__author__ = 'Brenden'

import sqlite3

conn = sqlite3.connect('Test.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Customer(CustomerID INTEGER, Hour INTEGER, Age INTEGER, Gender TEXT, Items TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Employee(Name TEXT, ClockIn INTEGER, ClockOut INTEGER, Wage INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS Products(ProductID INTEGER)')


create_table()
c.close()
conn.close()
