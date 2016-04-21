__author__ = 'Brenden'
import sqlite3
import pprint

####################################################################
# Holds functions to return different fields from the database     #
# Used for data analysis                                           #
# Needs to return values now                                       #
####################################################################

# proper input is as follows:
# startDate: entry in quotes and date and month must be 2 digits so january 1st would be 01-01.
#   full example: "01-02-2018"
# endData: same as startDate
# Employee, Customer, Product: just enter 1 or 0 for each. 1 means you want data 0 means no data
# as of now it just returns all of the data from the table but could be made to return only certain col's
class retrieveData:
    def __init__(self, date_range, employee, customer, product):
        # list for looping
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        startDate = date_range[0]
        endDate = date_range[1]
        print(startDate)
        print(endDate)
        # first to indices of input are month
        # this is why entries must be 2 digits for day and month
        startMonth = (startDate[0] + startDate[1])
        # indices 3 and 4 are day
        startDay = (startDate[3] + startDate[4])

        # removes leading 0 so it matches database
        if(int(startMonth[0]) == 0):
            startMonth = startMonth[1]


        endMonth = (endDate[0] + endDate[1])
        endDay = (endDate[3] + endDate[4])

        if(int(endMonth[0]) == 0):
            endMonth = endMonth[1]

        # list to store all the data returned
        all_data = {}
        final_data = {}

        # loop for only going thru 1 month
        if(int(startMonth) == int(endMonth)):
            for i in range(int(startDay), int(endDay) + 1):
                temp_name = (startMonth + "-" + str(i) + "-" + "2018")
                tempDB = (startMonth + "-" + str(i) + "-" + "2018.db")
                self.conn = sqlite3.connect(tempDB)
                self.c = self.conn.cursor()
                if(employee == 1):
                   all_data['Employee'] = self.get_employee_data()
                if(customer == 1):
                    all_data['Customer'] = self.get_customer_data()
                if(product == 1):
                    all_data['Product'] = self.get_product_data()
                final_data[temp_name] = all_data

        # loop for multiple months
        else:
            for i in range(int(startDay), days_in_month[(int(startMonth) - 1)] + 1):
                tempDB = (startMonth + "-" + str(i) + "-" + "2018.db")
                temp_name = (startMonth + "-" + str(i) + "-" + "2018")
                self.conn = sqlite3.connect(tempDB)
                self.c = self.conn.cursor()
                if(employee == 1):
                   all_data['Employee'] = self.get_employee_data()
                if(customer == 1):
                    all_data['Customer'] = self.get_customer_data()
                if(product == 1):
                    all_data['Product'] = self.get_product_data()
                final_data[temp_name] = all_data

            for a in range(int(startMonth) + 1, int(endMonth) + 1):

                if(a == int(endMonth)):
                    for j in range(1, int(endDay) + 1):
                        tempDB = (endMonth + "-" + str(j) + "-" + "2018.db")
                        temp_name = (endMonth + "-" + str(j) + "-" + "2018")
                        self.conn = sqlite3.connect(tempDB)
                        self.c = self.conn.cursor()
                        if(employee == 1):
                           all_data['Employee'] = self.get_employee_data()
                        if(customer == 1):
                            all_data['Customer'] = self.get_customer_data()
                        if(product == 1):
                            all_data['Product'] = self.get_product_data()
                        final_data[temp_name] = all_data


                else:
                    for k in range(1, days_in_month[(a - 1)] + 1):
                        tempDB = (str(a) + "-" + str(k) + "-" + "2018.db")
                        temp_name = (str(a) + "-" + str(k) + "-" + "2018")
                        self.conn = sqlite3.connect(tempDB)
                        self.c = self.conn.cursor()
                        if(employee == 1):
                           all_data['Employee'] = self.get_employee_data()
                        if(customer == 1):
                            all_data['Customer'] = self.get_customer_data()
                        if(product == 1):
                            all_data['Product'] = self.get_product_data()
                        final_data[temp_name] = all_data
        # print the data
        #print(all_data)
        #print(final_data)
        pprint.pprint(final_data)




    # enter 1 for parameters you want to get data for and 0 for the ones you dont want
    # ex: if you only want clockin and clockout time call get_employee_data(0,1,1,0)
    #def get_employee_data(self, name, clockin, clockout, wage):
    def get_employee_data(self):
        all_data1 = []
       # if name:
       #     evaluation.append("Name")

        #if clockin:
         #   evaluation.append("ClockIn")

        #if clockout:
         #   evaluation.append("ClockOut")

        #if wage:
           # evaluation.append("Wage")

        # make list into comma seperated string for use in database calls
        #x = ','.join(map(str, evaluation[1:]))

        #self.c.execute("SELECT " + x + " FROM Employee")
        self.c.execute("SELECT * FROM Employee")
        for row in self.c.fetchall():
                #print(row)
                all_data1.append(row)
        return all_data1

    #def get_customer_data(self, customerid, hour, age, gender, items):
    def get_customer_data(self):
       newlist = []
       #if customerid:
        #   newlist.append("CustomerID")

       #if hour:
        #   newlist.append("Hour")

       #if age:
        #   newlist.append("Age")

       #if gender:
        #   newlist.append("Gender")

       #if items:
        #   newlist.append("Items")

       #y = ','.join(map(str, newlist[1:]))

      # self.c.execute("SELECT "+y+" FROM Customer")
       self.c.execute("SELECT * FROM Customer")
       for row in self.c.fetchall():
               #print(row)
          newlist.append(row)

       return newlist

    #def get_product_data(self, productid, price):
    def get_product_data(self):
        productlist = []
        #if productid:
         #   productlist.append("ProductID")
        #if price:
         #   productlist.append("Price")
        #list_to_retrieve = ','.join(map(str, productlist[1:]))
        #self.c.execute("SELECT " + list_to_retrieve + " FROM Products")
        self.c.execute("SELECT * FROM Products")
        for row in self.c.fetchall():
            #print(row)
            productlist.append(row)
        return productlist

get_some_data = retrieveData(["01-30-2018", "02-03-2018"], 0, 0, 0)
#get_some_data.get_employee_data()
#get_some_data.get_customer_data(1, 1, 1, 1, 0)
#get_some_data.get_product_data(1,1)
