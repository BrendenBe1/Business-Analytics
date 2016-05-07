import sqlite3

class createDB:
    """
    Opens a new database connection
    Creates the tables needed to store data
    Closes connection
    Results in a database with empty fields that can be accessed later
    """

    def __init__(self, databaseName):
        """
        Creates the initial database and calls respective functions to create the tables and close the DB

        :param databaseName: string
        :return: none
        """

        print("\n------------| DATABASE CREATION |------------\n")
        self.database_name = databaseName

        # Create DB
        self.conn = sqlite3.connect(self.database_name)

        # Variable to access DB
        self.c = self.conn.cursor()

        print("> Database", self.database_name, "was created successfully")
        self.createTables()
        self.closeDB()


    def createTables(self):
        """
        Create CUSTOMER, EMPLOYEE, and PRODUCT tables

        :return: none
        """

        self.c.execute('CREATE TABLE IF NOT EXISTS Customer(CustomerID INTEGER, Hour INTEGER, Age INTEGER, Gender TEXT, Items TEXT)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Employee(Name TEXT, ClockIn INTEGER, ClockOut INTEGER, Wage INTEGER)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Products(ProductID INTEGER, Price INTEGER)')
        print(">", self.database_name, "has been organized into 3 tables successfully")


    def closeDB(self):
        """
        Save fields and allow other classes to access the database

        :return: none
        """

        self.c.close()
        self.conn.close()
        print(">", self.database_name, "is now closed")
        print("\n---------------------------------------------\n")

