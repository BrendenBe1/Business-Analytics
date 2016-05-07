from tkinter import *
from tkinter import ttk
import datetime
import dataAnalysis
import createDashboard

class GUI:
    def __init__(self):
        print("\n-----------------| GUI |-----------------\n")

        # Generate window
        self.root = Tk()
        self.root.title("Generate Graphs")
        self.root.maxsize(160, 300)
        self.root.minsize(160, 300)

        # Variables
        self.current_year = str(datetime.datetime.now().year)

        # ttk styles
        self.green_button = ttk.Style()
        self.green_button.map("TButton", foreground=[('pressed', 'white'), ('active', 'green')],  background=[('pressed', 'white'), ('active', 'white')])

        # Checkbox variables
        self.a = IntVar()
        self.b = IntVar()
        self.c = IntVar()
        self.d = IntVar()
        self.e = IntVar()
        self.f = IntVar()
        self.graphs = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.selected = [0, 0, 0, 0, 0, 0]

        # Entry variables
        self.date_text = StringVar()
        self.date_text2 = StringVar()

        # Checkboxes
        graph_photo = PhotoImage(file="selection.gif")
        self.graph_label = Label(self.root, image=graph_photo, pady=10).pack(anchor=W)
        self.graph_0 = ttk.Checkbutton(self.root, text="Employee information", variable=self.a, width=200, style="TCheckbutton").pack()
        self.graph_1 = ttk.Checkbutton(self.root, text="Paying Customers", variable=self.b, width=200).pack()
        self.graph_2 = ttk.Checkbutton(self.root, text="Customer statistics", variable=self.c, width=200).pack()
        self.graph_3 = ttk.Checkbutton(self.root, text="Revenue", variable=self.d, width=200).pack()
        self.graph_4 = ttk.Checkbutton(self.root, text="Items sold", variable=self.e, width=200).pack()
        self.graph_5 = ttk.Checkbutton(self.root, text="Extra statistics", variable=self.f, width=200).pack()

        # Entries
        self.date_photo = PhotoImage(file="date.gif")
        self.date_label = Label(self.root, image=self.date_photo, pady=10).pack()
        self.date_entry = ttk.Entry(self.root, textvariable=self.date_text).pack()
        self.date_entry2 = ttk.Entry(self.root, textvariable=self.date_text2).pack()

        # Blank label
        self.empty_label = Label(self.root, text="").pack()

        # Create button
        self.display = ttk.Button(self.root, text="Create", style="TButton", command=self.input_check).pack()
        #self.display = Button(self.frame, text="Generate", command=self.generate_graphs).pack(anchor=W)

        print("> Successfully created GUI")
        print("> Waiting for input")

        self.root.mainloop()


    # Check if user inputted all needed data and date is in correct format
    def input_check(self):
        # Parameters
        date = self.date_text.get()
        date2 = self.date_text2.get()

        # No date provided
        if not (date and date2):
            print("> ERROR: Please enter dates")
            print("-----------------------------------------")
            self.root.destroy()
            return

        # Incorrect date format
        try:
            if date[2] != "-" or date2[2] != "-":
                print("> ERROR: Please enter the dates in the correct format")
                print("-----------------------------------------")
                self.root.destroy()
                return

        except IndexError:
                print("> ERROR: Please enter a full dates in the correct format")
                print("-----------------------------------------")
                self.root.destroy()
                return

        # No graphs selected
        if (self.a.get() or self.b.get() or self.c.get() or self.d.get() or self.e.get() or self.f.get()) == 0:
            print("> ERROR: Please select at least one graph")
            print("-----------------------------------------")
            self.root.destroy()
            return

        # Check for valid date
        if date[0] == 0:
            month = date[1]
        else:
            month = date[0]+date[1]

        if date[3] == 0:
            day = date[4]
        else:
            day = date[3]+date[4]

        if date2[0] == 0:
            month2 = date2[1]
        else:
            month2 = date2[0]+date2[1]

        if date[3] == 0:
            day2 = date2[4]
        else:
            day2 = date2[3]+date2[4]

        # Invalid date
        try:
            datetime.datetime(year=int(self.current_year),month=int(month),day=int(day))
            datetime.datetime(year=int(self.current_year),month=int(month2),day=int(day2))
        except ValueError:
            print("> ERROR: Please enter a valid date")
            self.root.destroy()
            return

        for i in range(len(self.graphs)):
            if self.graphs[i].get() == 1:
                self.selected[i] = 1

        self.analyze_data(self.convert_date())


    def analyze_data(self, date_range):

        print("> Analyzing data and generating graphs, please wait")

        URLs = dataAnalysis.dataAnalysis(date_range, self.selected).graph_URLs
        createDashboard.createDashboard(URLs, date_range)

        # Close GUI after creation
        self.root.destroy()
        return


    # MM-DD, MM-DD to [MM-DD-YY, MM-DD-YY]
    def convert_date(self):
        date_range = []
        date = self.date_text.get()
        date2 = self.date_text2.get()
        date += "-"
        date += self.current_year
        date2 += "-"
        date2 += self.current_year
        date_range.append(date)
        date_range.append(date2)

        return date_range