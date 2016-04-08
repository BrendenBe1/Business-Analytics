import sqlite3

####################################
# Grabs data from every field      #
# Analyzes data                    #
# Stores data in a second database #
####################################


class dataAnalysis:
    def __init__(self, database):
        print("\n------------| DATA ANALYSIS |------------\n")
        self.database_name = database.database_name
        self.conn = sqlite3.connect(self.database_name)
        self.c = self.conn.cursor()
        print("> Successfully connected to", self.database_name)
        print("> Pending...")

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