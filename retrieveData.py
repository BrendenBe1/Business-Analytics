import sqlite3

class retrieveData:
    """
    Used to grab data fields from database over a certain date range
    """

    def __init__(self, date_range, employee, customer, product):
        """
        :param date_range: list of two strings
        :param employee: int
        :param customer: int
        :param product: int
        :return: large dictionary of data fields from database
        """

        # Referenced when converting between months
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Grab date data
        startDate = date_range[0]
        endDate = date_range[1]
        startMonth = (startDate[0] + startDate[1])
        startDay = (startDate[3] + startDate[4])

        # Removes leading 0 so it matches database
        if int(startMonth[0]) == 0:
            startMonth = startMonth[1]
        endMonth = (endDate[0] + endDate[1])
        endDay = (endDate[3] + endDate[4])
        if int(endMonth[0] == 0):
            endMonth = endMonth[1]

        # Store all returned data
        all_data = {}
        self.final_data = {}

        # Loop for going through a single month
        if int(startMonth) == int(endMonth):
            for i in range(int(startDay), int(endDay) + 1):
                temp_name = (startMonth + "-" + str(i) + "-" + "2016")
                tempDB = (startMonth + "-" + str(i) + "-" + "2016.db")
                self.conn = sqlite3.connect(tempDB)
                self.c = self.conn.cursor()
                if employee:
                   all_data['Employee'] = self.get_employee_data()
                if customer:
                    all_data['Customer'] = self.get_customer_data()
                if product:
                    all_data['Product'] = self.get_product_data()
                self.final_data[temp_name] = all_data

        # Loops for going through multiple months
        else:
            for i in range(int(startDay), days_in_month[(int(startMonth) - 1)] + 1):
                tempDB = (startMonth + "-" + str(i) + "-" + "2016.db")
                temp_name = (startMonth + "-" + str(i) + "-" + "2016")
                self.conn = sqlite3.connect(tempDB)
                self.c = self.conn.cursor()
                if employee:
                   all_data['Employee'] = self.get_employee_data()
                if customer:
                    all_data['Customer'] = self.get_customer_data()
                if product:
                    all_data['Product'] = self.get_product_data()
                self.final_data[temp_name] = all_data

            for a in range(int(startMonth) + 1, int(endMonth) + 1):
                if a == int(endMonth):
                    for j in range(1, int(endDay) + 1):
                        tempDB = (endMonth + "-" + str(j) + "-" + "2016.db")
                        temp_name = (endMonth + "-" + str(j) + "-" + "2016")
                        self.conn = sqlite3.connect(tempDB)
                        self.c = self.conn.cursor()
                        if employee:
                           all_data['Employee'] = self.get_employee_data()
                        if customer:
                            all_data['Customer'] = self.get_customer_data()
                        if product:
                            all_data['Product'] = self.get_product_data()
                        self.final_data[temp_name] = all_data

                else:
                    for k in range(1, days_in_month[(a - 1)] + 1):
                        tempDB = (str(a) + "-" + str(k) + "-" + "2016.db")
                        temp_name = (str(a) + "-" + str(k) + "-" + "2016")
                        self.conn = sqlite3.connect(tempDB)
                        self.c = self.conn.cursor()
                        if employee:
                           all_data['Employee'] = self.get_employee_data()
                        if customer:
                            all_data['Customer'] = self.get_customer_data()
                        if product:
                            all_data['Product'] = self.get_product_data()
                        self.final_data[temp_name] = all_data


    def get_employee_data(self):
        """
        :return: list of employee data
        """

        employee_list = []
        self.c.execute("SELECT * FROM Employee")
        for row in self.c.fetchall():
                employee_list.append(row)
        return employee_list


    def get_customer_data(self):
        """
        :return: list of customer data
        """

        customer_list = []
        self.c.execute("SELECT * FROM Customer")
        for row in self.c.fetchall():
           customer_list.append(row)
        return customer_list


    def get_product_data(self):
        """
        :return: dict of products (ID : price)
        """

        product_list = {}
        self.c.execute("SELECT * FROM Products")
        for row in self.c.fetchall():
            product_list.update({row[0]: row[1]})
        return product_list

