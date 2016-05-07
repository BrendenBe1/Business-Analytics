import retrieveData
import plotly.plotly as py
import collections
from plotly.graph_objs import *
from random import randint

class dataAnalysis:
    """
    Analyzes data from the database and creates individual graphs
    """

    def __init__(self, date_range, selected):
        """
        Checks with GUI to determine which graphs the user wants, then calls the respective graphing functions

        :param date_range: list of two strings
        :param selected: list of ints
        :return: none
        """

        print("\n------------| DATA ANALYSIS |------------\n")
        print("> Grabbing data from GUI")
        self.date_range = date_range
        self.graph_URLs = []
        self.dates = []
        self.convert_date_range()
        self.database = retrieveData.retrieveData(date_range, 1, 1, 1).final_data

        self.employee_hours_dict = {}
        self.employee_hours_dict2 = {}
        self.employee_pay_dict = {}

        # Selected graphs
        if selected[0]:
            self.employee_hours()
            self.employee_pay()

        if selected[1]:
            self.ratio_data = {'Paying' : {'Total' : 0,
                                           'Male' : 0,
                                           'Female' : 0,
                                           'Age groups' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}},
                               'Nonpaying' : {'Total' : 0,
                                              'Male' : 0,
                                              'Female' : 0,
                                              'Age groups' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}}}
            self.customer_ratio()

        if selected[2]:
            self.category_purchases = {'Food' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Electronics' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Outdoors' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Clothing' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}, 'Beauty' : {"18-23" : 0, "24-29" : 0, "30-35" : 0, "36-41" : 0, "42-47" : 0, "48-53" : 0, "54-59" : 0, "60-65" : 0, "65+" : 0}}
            self.category_genders = {'Food' : {'M' : 0, 'F' : 0}, 'Electronics' : {'M' : 0, 'F' : 0}, 'Outdoors' : {'M' : 0, 'F' : 0}, 'Clothing' : {'M' : 0, 'F' : 0}, 'Beauty' : {'M' : 0, 'F' : 0}}
            self.age_gender_paying()

        if selected[3]:
            self.revenue()
            pass



    def convert_age_group(self, age):
        """
        Places a given age into a range, and returns that range

        :param age: int
        :return: string
        """

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


    def convert_date_range(self):
        """
        Enumerates a list of all dates between two dates given

        :return: list
        """

        # Separate list
        startDate = self.date_range[0]
        startDay = (startDate[3] + startDate[4])
        startMonth = (startDate[0] + startDate[1])

        # Remove leading 0
        if int(startMonth[0]) == 0:
            startMonth = startMonth[1]

        # Separate list
        endDate = self.date_range[1]
        endMonth = (endDate[0] + endDate[1])
        endDay = (endDate[3] + endDate[4])

        # Remove leading 0
        if int(endMonth[0]) == 0:
            endMonth = endMonth[1]

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Same month
        if int(startMonth) == int(endMonth):
            for i in range(int(startDay), int(endDay) + 1):
                temp_name = (startMonth + "-" + str(i) + "-" + "2016")
                self.dates.append(temp_name)

        # Different months
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


    def calculate_employee_pay(self):
        """
        Modifies a public dictionary that holds employees and their respective pay over a date range

        :return: none
        """

        # Ignore dates because employee wage is static
        for j in range(len(self.database[self.dates[0]]['Employee'])):
            temp_employee = self.database[self.dates[0]]['Employee'][j]
            pay = temp_employee[3]
            self.employee_pay_dict[temp_employee[0]] = pay*self.employee_hours_dict[temp_employee[0]]


    def calculate_employee_hours(self):
        """
        Modifies a public dictionary that holds employees and their respective hours worked over a date range

        :return: none
        """

        # Go through every date
        for i in range(len(self.dates)):

            # Go through every employee
            for j in range(len(self.database[self.dates[0]]['Employee'])):

                # Grab hours worked
                temp_employee = self.database[self.dates[i]]['Employee'][j]
                hours_worked = temp_employee[2] - temp_employee[1]

                # Store hours worked
                if temp_employee[0] not in self.employee_hours_dict:
                    self.employee_hours_dict[temp_employee[0]] = hours_worked
                else:
                    self.employee_hours_dict[temp_employee[0]] += hours_worked


    def employee_pay(self):
        """
        Generates a bar graph of employee pay and appends the URL to a public list

        :return: none
        """

        print("> Analyzing Employee Pay...")

        self.calculate_employee_pay()

        # Holds graph objects
        graph_list = []

        # Generate graph objects
        for data in self.employee_pay_dict:
            tmp = Bar(x=data, y=self.employee_pay_dict[data], name=data)
            graph_list.append(tmp)

        # Call API to generate graph URLs
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Pay", xaxis=dict(title='Employee'), yaxis=dict(title='USD paid'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Pay')
        self.graph_URLs.append(graph_uniqueURL)


    def employee_hours(self):
        """
        Generates a bar graph of employee hours and appends the URL to a public list

        :return: none
        """

        print("> Analyzing Employee Hours...")

        self.calculate_employee_hours()
        graph_list = []
        for data in self.employee_hours_dict:
            tmp = Bar(x=data, y=self.employee_hours_dict[data], name=data)
            graph_list.append(tmp)

        # Generate graph
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Employee Hours", xaxis=dict(title='Employee'), yaxis=dict(title='Hours worked'))
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Employee-Hours')
        self.graph_URLs.append(graph_uniqueURL)


    def customer_ratio(self):
        """
        Generates 3 stacked bar graphs

        One bar represents the number of paying customers. The other represents customers who did not pay
        The second graph breaks down the genders
        The third graph breaks down the age groups

        :return: none
        """

        # Go through every date
        for i in range(len(self.dates)):

            # Go through every customer
            for j in range(len(self.database[self.dates[0]]['Customer'])):

                # Grab customer data
                temp_customer = self.database[self.dates[i]]['Customer'][j]

                # Purchases
                if temp_customer[4]:
                    self.ratio_data['Paying']['Total'] += 1

                    if temp_customer[3] == 'M':
                        self.ratio_data['Paying']['Male'] += 1
                    else:
                        self.ratio_data['Paying']['Female'] += 1

                    # Increment age group
                    self.ratio_data['Paying']['Age groups'][self.convert_age_group(temp_customer[2])] += 1

                else:
                    self.ratio_data['Nonpaying']['Total'] += 1
                    if temp_customer[3] == 'M':
                        self.ratio_data['Nonpaying']['Male'] += 1
                    else:
                        self.ratio_data['Nonpaying']['Female'] += 1
                    self.ratio_data['Nonpaying']['Age groups'][self.convert_age_group(temp_customer[2])] += 1

        # Generate total ratio
        graph_list = []
        tmp = Bar(x='Ratio', name='Paying', y=self.ratio_data['Paying']['Total'])
        graph_list.append(tmp)
        tmp = Bar(x='Ratio', name='Non-paying', y=self.ratio_data['Nonpaying']['Total'])
        graph_list.append(tmp)
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Paying and non-paying customers")
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Customer-Ratio')
        self.graph_URLs.append(graph_uniqueURL)

        # Generate gender ratio
        graph_list = []
        tmp = Bar(x='Ratio', name='Male', y=self.ratio_data['Paying']['Male'])
        graph_list.append(tmp)
        tmp = Bar(x='Ratio', name='Female', y=self.ratio_data['Paying']['Female'])
        graph_list.append(tmp)
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Genders of paying customers")
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Gender-Ratio')
        self.graph_URLs.append(graph_uniqueURL)

        # Generate age ratio
        graph_list = []
        for group in self.ratio_data['Paying']['Age groups']:
            graph_list.append(Bar(x='Ratio', name=group, y=self.ratio_data['Paying']['Age groups'][group]))
        graph_data = Data(graph_list)
        graph_layout = Layout(barmode='stack', title="Ages of paying customers")
        graph_fig = Figure(data=graph_data, layout=graph_layout)
        graph_uniqueURL = py.plot(graph_fig, filename='Age-Ratio')
        self.graph_URLs.append(graph_uniqueURL)



    def age_gender_paying(self):
        """
        Generates many pie graphs that represent which age groups and genders purchased from each category

        :return: none
        """

        for i in range(len(self.dates)):
            for j in range(len(self.database[self.dates[0]]['Customer'])):

                # Analysis for pie graphs
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


    def revenue(self):
        """
        Generates 3 scatter plots that represent revenue, profit, and losses

        :return: none
        """

        self.calculate_employee_hours()
        self.calculate_employee_pay()

        profit_graph_list = []
        revenue_graph_list = []
        losses_graph_list = []

        # Customer purchases
        for i in range(len(self.dates)):
            daily_revenue = 0
            losses = 0

            for j in range(len(self.database[self.dates[0]]['Employee'])):
                try:
                    temp_employee = self.database[self.dates[i]]['Employee'][i]
                    losses += (temp_employee[2] - temp_employee[1]) * temp_employee[3]
                except IndexError:
                    losses += randint(40, 300)

            # Go through every customer
            for k in range(len(self.database[self.dates[0]]['Customer'])):

                # Analysis
                temp_customer = self.database[self.dates[i]]['Customer'][k]
                purchased_items = temp_customer[4].split(", ")

                # Add price of purchased item
                for item in purchased_items:
                    try:
                        daily_revenue += self.database[self.dates[i]]['Product'][int(item)]
                    except ValueError: # ['']
                        pass

            profit = daily_revenue - losses
            profit_graph_list.append(Scatter(x=self.dates[i], y=profit, name="Profit", line=dict(color=('rgb(22, 96, 197)'), width=4, dash='dash')))
            revenue_graph_list.append(Scatter(x=self.dates[i], y=daily_revenue, name="Revenue", line=dict(color=('rgb(22, 96, 197)'), width=4, dash='dash')))
            losses_graph_list.append(Scatter(x=self.dates[i], y=losses, name="Losses", line=dict(color=('rgb(22, 96, 197)'), width=4, dash='dash')))

        # Edit the layout
        layout1 = dict(title = 'Profit',
                      xaxis = dict(title = 'Date'),
                      yaxis = dict(title = 'USD'),
                      )

        layout2 = dict(title = 'Revenue',
                      xaxis = dict(title = 'Date'),
                      yaxis = dict(title = 'USD'),
                      )

        layout3 = dict(title = 'Losses',
                      xaxis = dict(title = 'Date'),
                      yaxis = dict(title = 'USD'),
                      )

        # Plot
        fig1 = dict(data=profit_graph_list, layout=layout1)
        fig2 = dict(data=revenue_graph_list, layout=layout2)
        fig3 = dict(data=losses_graph_list, layout=layout3)
        URL1 = py.plot(fig1, filename='profit')
        URL2 = py.plot(fig2, filename='revenue')
        URL3 = py.plot(fig3, filename='losses')
        self.graph_URLs.append(URL1)
        self.graph_URLs.append(URL2)
        self.graph_URLs.append(URL3)