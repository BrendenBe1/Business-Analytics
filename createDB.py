import sqlite3

############################################################
# Opens a new database connection                          #
# Creates the tables needed to store data                  #
# Closes connection                                        #
# Results in an empty database that can be accesses later  #
############################################################

class createDB:

    # Constructor creates the initial database and calls respective functions to create the tables and close the DB
    def __init__(self, databaseName):
        print("\n------------| DATABASE CREATION |------------\n")
        self.database_name = databaseName
        self.conn = sqlite3.connect(self.database_name)  # Create DB
        self.c = self.conn.cursor()  # Variable to access DB
        print("> Database", self.database_name, "was created successfully")
        self.createTables()
        self.closeDB()

    # Create CUSTOMER, EMPLOYEE, PRODUCT tables
    def createTables(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Customer(CustomerID INTEGER, Hour INTEGER, Age INTEGER, Gender TEXT, Items TEXT)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Employee(Name TEXT, ClockIn INTEGER, ClockOut INTEGER, Wage INTEGER)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Products(ProductID INTEGER, Price INTEGER)')
        print(">", self.database_name, "has been organized into 3 tables successfully")

    # Save fields and allow other classes to access DB
    def closeDB(self):
        self.c.close()
        self.conn.close()
        print(">", self.database_name, "is now closed")
        print("\n---------------------------------------------\n")

