import sqlite3

####################################################################
# Holds functions to return different fields from the database     #
# Used for data analysis                                           #
# Needs to return values now                                       #
####################################################################


class retrieveData:
    def __init__(self):
        self.conn = sqlite3.connect('DataAnalysis.db')
        self.c = self.conn.cursor()

    # enter 1 for parameters you want to get data for and 0 for the ones you dont want
    # ex: if you only want clockin and clockout time call get_employee_data(0,1,1,0)
    def get_employee_data(self, name, clockin, clockout, wage):
        evaluation = [0]
        if name:
            evaluation.append("Name")

        if clockin:
            evaluation.append("ClockIn")

        if clockout:
            evaluation.append("ClockOut")

        if wage:
            evaluation.append("Wage")

        # make list into comma seperated string for use in database calls
        x = ','.join(map(str, evaluation[1:]))

        self.c.execute("SELECT "+x+" FROM Employee")
        for row in self.c.fetchall():
                print(row)

    def get_customer_data(self, customerid, hour, age, gender, items):
       newlist = [0]
       if customerid:
           newlist.append("CustomerID")

       if hour:
           newlist.append("Hour")

       if age:
           newlist.append("Age")

       if gender:
           newlist.append("Gender")

       if items:
           newlist.append("Items")

       y = ','.join(map(str, newlist[1:]))

       self.c.execute("SELECT "+y+" FROM Customer")
       for row in self.c.fetchall():
           print(row)

    def get_product_data(self, productid):
        if productid:
            self.c.execute("Select ProductID FROM Products")
            for row in self.c.fetchall():
                print(row)

get_some_data = retrieveData()
get_some_data.get_employee_data(1, 1, 1, 0)
#get_some_data.get_customer_data(1, 1, 1, 1, 0)
#get_some_data.get_product_data(1)
