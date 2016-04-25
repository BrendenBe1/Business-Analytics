import sqlite3
import retrieveData
import plotly.plotly as py
from plotly.graph_objs import *

####################################
# Grabs data from every field      #
# Analyzes data                    #
# Stores data in a second database #
####################################

#TODO:
# Grab data from GUI
# Pass data into parameters
# Translate data into needed database parameters
# Grab respective data from databases
# Analyze

class dataAnalysis:
    def __init__(self, date_range, selected):
        print("\n------------| DATA ANALYSIS |------------\n")
        print("> Grabbing data from GUI")
        self.date_range = date_range
        self.graph_URLs = []
        self.dates = []
        self.convert_date_range()
        self.database = retrieveData.retrieveData(date_range, 1, 1, 1).final_data

        # Selected graphs
        if selected[0]:
            self.employee_hours_dict = {}
            self.employee_pay_dict = {}
            self.employee_hours()
            self.employee_pay()

        if selected[1]:
            self.paying = 0
            self.nonpaying = 0
            self.customer_ratio()
            pass

        if selected[2]:
          #  self.
            pass

        if selected[3]:
            pass

        if selected[4]:
            pass

        if selected[5]:
            pass


    # Returns a list of all dates between the two given
    def convert_date_range(self):

        startDate = self.date_range[0]
        startDay = (startDate[3] + startDate[4])
        startMonth = (startDate[0] + startDate[1])

        if int(startMonth[0]) == 0:
            startMonth = startMonth[1]

        endDate = self.date_range[1]
        endMonth = (endDate[0] + endDate[1])
        endDay = (endDate[3] + endDate[4])

        if int(endMonth[0]) == 0:
            endMonth = endMonth[1]

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if(int(startMonth) == int(endMonth)):
            for i in range(int(startDay), int(endDay) + 1):
                temp_name = (startMonth + "-" + str(i) + "-" + "2016")
                self.dates.append(temp_name)

        else:
            for i in range(int(startDay), days_in_month[(int(startMonth) - 1)] + 1):
                temp_name = (startMonth + "-" + str(i) + "-" + "2016")
                self.dates.append(temp_name)


            for a in range(int(startMonth) + 1, int(endMonth) + 1):

                if a == int(endMonth):
                    for j in range(1, int(endDay) + 1):
                        temp_name = (endMonth + "-" + str(j) + "-" + "2016")
                        self.dates.append(temp_name)
                else:
                    for k in range(1, days_in_month[(a - 1)] + 1):
                        temp_name = (str(a) + "-" + str(k) + "-" + "2016")
                        self.dates.append(temp_name)
        #print("Dates:", self.dates)


    def employee_pay(self):
        print("> Analyzing Employee Pay...")
        print("     > Result: ", end='')

        # Grab dictionary
        for j in range(len(self.database[self.dates[0]]['Employee'])):
            temp_employee = self.database[self.dates[0]]['Employee'][j]
            pay = temp_employee[3]
            self.employee_pay_dict[temp_employee[0]] = pay*self.employee_hours_dict[temp_employee[0]]

        # Generate data points with above data struct
        graph_list = []

        for data in self.employee_pay_dict:
            tmp = Bar(x=data, y=self.employee_pay_dict[data], name=data)
            graph_list.append(tmp)

        print(self.employee_pay_dict)
        # Make graph
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Pay", xaxis=dict(title='Employee'), yaxis=dict(title='USD paid'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
       # graph_uniqueURL = py.plot(graph_fig, filename='Employee-Pay')
      #  self.graph_URLs.append(graph_uniqueURL)


    def employee_hours(self):

        print("> Analyzing Employee Hours...")
        print("     > Result: ", end='')

        for i in range(len(self.dates)):
            for j in range(len(self.database[self.dates[0]]['Employee'])):
                temp_employee = self.database[self.dates[i]]['Employee'][j]
                hours_worked = temp_employee[2] - temp_employee[1]

                if temp_employee[0] not in self.employee_hours_dict:
                    self.employee_hours_dict[temp_employee[0]] = hours_worked
                else:
                    self.employee_hours_dict[temp_employee[0]] += hours_worked

        print(self.employee_hours_dict)
        graph_list = []
        for data in self.employee_hours_dict:
            tmp = Bar(x=data, y=self.employee_hours_dict[data], name=data)
            graph_list.append(tmp)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Hours", xaxis=dict(title='Employee'), yaxis=dict(title='Hours worked'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
      #  graph_uniqueURL = py.plot(graph_fig, filename='Employee-Hours')
      #  self.graph_URLs.append(graph_uniqueURL)


    def customer_ratio(self):
        for i in range(len(self.dates)):
            for j in range(len(self.database[self.dates[0]]['Customer'])):

                # Analysis goes here
                temp_customer = self.database[self.dates[i]]['Customer'][j]
                if temp_customer[4]:
                    self.paying += 1
                else:
                    self.nonpaying += 1

        print(self.nonpaying)
        graph_list = []

        tmp = Bar(x='Ratio', name='Paying', y=self.paying)
        graph_list.append(tmp)

        tmp = Bar(x='Ratio', name='Non-paying', y=self.nonpaying)
        graph_list.append(tmp)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Paying and non-paying customers")
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Customer-Ratio')
        self.graph_URLs.append(graph_uniqueURL)


    def age_gender_paying(self):
        for i in range(len(self.dates)):
            for j in range(len(self.database[self.dates[0]]['Customer'])):

                # Analysis goes here
                temp_customer = self.database[self.dates[i]]['Customer'][j]

                if temp_customer[4]:
                    self.paying += 1

        print(self.nonpaying)
        graph_list = []

        tmp = Bar(x='Ratio', name='Paying', y=self.paying)
        graph_list.append(tmp)

        tmp = Bar(x='Ratio', name='Non-paying', y=self.nonpaying)
        graph_list.append(tmp)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Paying and non-paying customers")
        graph_fig = Figure(data=graph_data, layout=graph_layout)

    # Age and Gender of paying customers per hour
        # DATA: CUSTOMER ALL
        # Stacked bar chart
        # The number or percentage of age categories that are paying customers
            # Along with the number or percentage of each gender that are paying customer

    # Purchases by category (age and gender)
        # DATA: PRODUCTS
        # Single graph or two graphs
        # The number of purchases by category by both the age and gender of customers

    # Revenue
        # DATA: EMPLOYEES CLOCK IN / CLOCK OUT / WAGE
        # DATA: CUSTOMERS ITEMS
        # DATA: PRODUCTS ALL
        # Certain time period
        # Relationships between time periods, revenue, and loss
