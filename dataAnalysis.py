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
# Graph to dashboard(?)

class dataAnalysis:
    def __init__(self):
        print("\n------------| DATA ANALYSIS |------------\n")
        self.database = retrieveData.retrieveData()
      #  print("> Successfully connected to", self.database_name)
        print("> Pending...")
       # self.employee_hours()

    def employee_hours(self):

        # Grab dictionary
  #      self.database.get_employee_data(1, 1, 1, 0)

        # Analyze information + store into new data struct

        # Generate data points with above data struct
        graph_list = []
        employees = {"Zach Kramer" : 50, "Matt Kramer" : 60, "Spencer Cote" : 13}
        for data in employees:
            tmp = Bar(x=data, y=employees[data], name=data)
            graph_list.append(tmp)


        # Make graph
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack')
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Hours')



    def employee_pay(self):
        # self.database.get_employee_data

        graph_list = []
        employees = {}
        for data in employees:
            tmp = Bar(x=data, y=employees[data], name=data)
            graph_list.append(tmp)

        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack')
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Pay')






    # Fields to analyze

    # Employee hours
        # DATA: EMPLOYEE CLOCK IN / CLOCK OUT
        # Grouped bar chart with each bar in a group representing an employee
        # Number of hours each employee has worked over a period of time

    # Employee pay
        # DATA: EMPLOYEE CLOCK IN / CLOCK OUT / WAGE
        # Grouped bar chart with each bar representing an employee
        # How much each employee has been paid over a certain time period

    # Paying and non-paying customers per hour
        # DATA: CUSTOMER HOUR / ITEMS
        # Stacked bar chart (ratio of paying to non paying)
        # Represents ratio of paying to non paying

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

test = dataAnalysis()
test.employee_hours()