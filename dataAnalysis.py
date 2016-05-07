import sqlite3
import retrieveData
import plotly.plotly as py
import collections
from plotly.graph_objs import *
from random import randint

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

        self.employee_hours_dict = {}
        self.employee_pay_dict = {}
        self.total_revenue = []

        # Selected graphs
        if selected[0]:
            self.employee_hours()
            self.employee_pay()

        if selected[1]:
            self.paying = 0
            self.nonpaying = 0
            self.customer_ratio()

        if selected[2]:
            self.category_purchases = {'Food' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Electronics' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Outdoors' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Clothing' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Beauty' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}}
            self.category_genders = {'Food' : {'M' : 0, 'F' : 0}, 'Electronics' : {'M' : 0, 'F' : 0}, 'Outdoors' : {'M' : 0, 'F' : 0}, 'Clothing' : {'M' : 0, 'F' : 0}, 'Beauty' : {'M' : 0, 'F' : 0}}
            self.age_gender_paying()

        if selected[3]:

            self.revenue()
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


    def employee_pay(self):
        print("> Analyzing Employee Pay...")
        print("     > Result: ", end='')

        self.calculate_employee_pay()

        # Generate data points with above data struct
        graph_list = []

        for data in self.employee_pay_dict:
            tmp = Bar(x=data, y=self.employee_pay_dict[data], name=data)
            graph_list.append(tmp)

        # Make graph
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Pay", xaxis=dict(title='Employee'), yaxis=dict(title='USD paid'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Pay')
        self.graph_URLs.append(graph_uniqueURL)


    def calculate_employee_hours(self):
        for i in range(len(self.dates)):
            for j in range(len(self.database[self.dates[0]]['Employee'])):
                temp_employee = self.database[self.dates[i]]['Employee'][j]
                hours_worked = temp_employee[2] - temp_employee[1]

                if temp_employee[0] not in self.employee_hours_dict:
                    self.employee_hours_dict[temp_employee[0]] = hours_worked
                else:
                    self.employee_hours_dict[temp_employee[0]] += hours_worked


    def calculate_employee_pay(self):

        # Grab dictionary
        for j in range(len(self.database[self.dates[0]]['Employee'])):
            temp_employee = self.database[self.dates[0]]['Employee'][j]
            pay = temp_employee[3]
            self.employee_pay_dict[temp_employee[0]] = pay*self.employee_hours_dict[temp_employee[0]]


    def employee_hours(self):

        print("> Analyzing Employee Hours...")
        print("     > Result: ", end='')

        self.calculate_employee_hours()

        print(self.employee_hours_dict)
        graph_list = []
        for data in self.employee_hours_dict:
            tmp = Bar(x=data, y=self.employee_hours_dict[data], name=data)
            graph_list.append(tmp)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Hours", xaxis=dict(title='Employee'), yaxis=dict(title='Hours worked'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Hours')
        self.graph_URLs.append(graph_uniqueURL)


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
                temp_list = temp_customer[4].split(', ')

                for purchaseID in temp_list:
                    if purchaseID:
                        category = int(purchaseID[0])
                        if category == 1:
                            key = 'Food'
                        elif category == 2:
                            key = 'Electronics'
                        elif category == 3:
                            key = 'Outdoors'
                        elif category == 4:
                            key = 'Clothing'
                        elif category == 5:
                            key = 'Beauty'

                        # Age : purchases
                        self.category_purchases[key][self.convert_age_group(temp_customer[2])] += 1
                        self.category_genders[key][temp_customer[3]] += 1

        for category in self.category_purchases:
            values = []
            labels = []
            for group in self.category_purchases[category]:
                values.append(self.category_purchases[category][group])
                labels.append(group)
            print(values)
            fig = {
              'data': [{'labels': labels,
              'values': values,
              'type': 'pie'}],
              'layout': {'title': category + ' purchases by age group'}
                }
            url = py.plot(fig)
            self.graph_URLs.append(url)

        graph_list = []
        for category in self.category_genders:
            tmp = Bar(x=category, name='Male', y=self.category_genders[category]['M'])
            tmp2 = Bar(x=category, name='Female', y=self.category_genders[category]['F'])
            graph_list.append(tmp)
            graph_list.append(tmp2)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Purchases by gender")
        graph_fig = Figure(data=graph_data, layout=graph_layout)

        graph_uniqueURL = py.plot(graph_fig)
        self.graph_URLs.append(graph_uniqueURL)

    def convert_age_group(self, age):
        if 18 <= age <= 23:
            age_group = "18-23"
        elif 24 <= age <= 29:
            age_group = "24-29"
        elif 30 <= age <= 35:
            age_group = "30-35"
        elif 36 <= age <= 41:
            age_group = "36-41"
        elif 42 <= age <= 47:
            age_group = "42-47"
        elif 48 <= age <= 53:
            age_group = "48-53"
        elif 54 <= age <= 59:
            age_group = "54-59"
        elif 60 <= age <= 65:
            age_group = "60-65"
        elif age > 65:
            age_group = "65+"
        return age_group


    def revenue(self):
        self.calculate_employee_hours()
        self.calculate_employee_pay()
        print(self.employee_hours_dict)
        print(self.employee_pay_dict)

        losses = 0

        # Employee wage * hours
        for employee in self.employee_hours_dict:
            self.total_revenue.append(self.employee_hours_dict[employee] * self.employee_pay_dict[employee])

        # Customer purchases
        total_purchase_revenue = 0
        for i in range(len(self.dates)):

            # Current database doesn't account for losses (and doesn't have to in our scope), so this variable is a temporary placeholder to show graph
            losses += randint(100, 1250)

            for j in range(len(self.database[self.dates[0]]['Customer'])):

                # Analysis goes here
                temp_customer = self.database[self.dates[i]]['Customer'][j]
                purchased_items = temp_customer[4].split(", ")
                for item in purchased_items:
                    try:
                        total_purchase_revenue += self.database[self.dates[i]]['Product'][int(item)]
                    except ValueError: # ['']
                        pass

            # Put everything here
                    # each x is a date

        self.total_revenue.append(total_purchase_revenue)
        revenue = sum(self.total_revenue)
        profit = revenue - losses

       # profit_graph = Scatter(x = "Profit", y=profit, name="Profit"

        print("The total revenue with no losses accounted for:", sum(self.total_revenue))



    # Age and Gender of paying customers per hour
        # DATA: CUSTOMER ALL
        # Stacked bar chart
        # The number or percentage of age categories that are paying customers
            # Along with the number or percentage of each gender that are paying customer


    # Revenue
        # DATA: EMPLOYEES CLOCK IN / CLOCK OUT / WAGE
        # DATA: CUSTOMERS ITEMS
        # DATA: PRODUCTS ALL
        # Certain time period
        # Relationships between time periods, revenue, and loss
