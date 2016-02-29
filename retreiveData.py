__author__ = 'Brenden'
import sqlite3

conn = sqlite3.connect('DataAnalysis.db')
c = conn.cursor()


def read_from_db():
    #c.execute('SELECT * FROM Employee')  # selects everything
    #c.execute('SELECT * FROM Employee WHERE ClockIn=19') # selects only the places where clockin == 19
    c.execute('SELECT * FROM Employee WHERE ClockIn=19 AND Wage=12') # selects only places with 2 conditions
    # print it all raw
    #data = c.fetchall()
    #print(data)

    # print each row
    for row in c.fetchall():
        print(row)

    print('--------------------------')

    c.execute('SELECT * FROM Customer WHERE Gender="M" AND Hour=21 AND Age=21 ')
    for row in c.fetchall():
        print(row)

    print('--------------------------')

    c.execute('SELECT * FROM Products WHERE ProductID < 10500 ')
    for row in c.fetchall():
        print(row)


read_from_db()
c.close()
conn.close()