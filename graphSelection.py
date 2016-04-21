from tkinter import *
from tkinter import ttk
import datetime

class GUI:
    def __init__(self):
        print("\n-----------------| GUI |-----------------\n")

        # Generate window
        self.root = Tk()
        self.root.title("Generate Graphs")
        self.root.maxsize(160, 380)
        self.root.minsize(160, 380)

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
        self.selected = []

        # Radiobutton variable
        self.date_type = IntVar()

        # Entry variables
        self.date_text = StringVar()

        # Checkboxes
        graph_photo = PhotoImage(file="selection.gif")
        self.graph_label = Label(self.root, image=graph_photo, pady=10).pack(anchor=W)
        self.graph_0 = ttk.Checkbutton(self.root, text="Employee information", variable=self.a, width=200, style="TCheckbutton").pack()
        self.graph_1 = ttk.Checkbutton(self.root, text="# of customers per hour", variable=self.b, width=200).pack()
        self.graph_2 = ttk.Checkbutton(self.root, text="Daily customer statistics", variable=self.c, width=200).pack()
        self.graph_3 = ttk.Checkbutton(self.root, text="Revenue", variable=self.d, width=200).pack()
        self.graph_4 = ttk.Checkbutton(self.root, text="Items sold", variable=self.e, width=200).pack()
        self.graph_5 = ttk.Checkbutton(self.root, text="Extra statistics", variable=self.f, width=200).pack()

        # Radiobuttons
        radio_photo = PhotoImage(file="time.gif")
        self.radio_label = Label(self.root, image=radio_photo, pady=10).pack(anchor=W)
        self.daily_button = ttk.Radiobutton(self.root, text="Day", variable=self.date_type, value = 1).pack()
        self.weekly_button = ttk.Radiobutton(self.root, text="Week", variable=self.date_type, value = 2).pack()
        self.monthly_button = ttk.Radiobutton(self.root, text="Month", variable=self.date_type, value = 3).pack()
        self.year_button = ttk.Radiobutton(self.root, text="Current year", variable=self.date_type, value = 4).pack()

        # Entry
        self.date_photo = PhotoImage(file="date.gif")
        self.date_label = Label(self.root, image=self.date_photo, pady=10).pack()
        self.date_entry = ttk.Entry(self.root, textvariable=self.date_text).pack()

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
        date_type = self.date_type.get() # 1, 2, 3, 4 = day, week, month, year
        # self.selected (graphs are 0-5)

        # No date provided
        if not date:

            # Year was selected
            if date_type == 4:
                pass

            # Close
            else:
                print("> ERROR: Please enter a date if you did not select current year")
                print("-----------------------------------------")
                self.root.destroy()
                return

        # Incorrect date format
        try:
            if date[2] != "-":
                print("> ERROR: Please enter the date in the correct format")
                print("-----------------------------------------")
                self.root.destroy()
                return

        except IndexError:
                print("> ERROR: Please enter a full date in the correct format")
                print("-----------------------------------------")
                self.root.destroy()
                return

        # Date type not selected
        if date_type not in [1,2,3,4]:
            print("> ERROR: Please select a date type")
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

        # Invalid date
        try:
            datetime.datetime(year=int(self.current_year),month=int(month),day=int(day))
        except ValueError:
            print("> ERROR: Please enter a valid date")
            self.root.destroy()
            return

        # Success
        print("> The following graphs were selected: ", end='')
        for graph in range(6):
            if self.graphs[graph].get():
                self.selected.append(graph)
                print(graph, end=' ')

        self.analyze_data(self.convert_date())


    def analyze_data(self, date_range):

        print("\n> Analyzing data, please wait")

        self.convert_date()

        print("\n> Generating graphs, please wait")


        #TODO: Call dataAnalysis on selected graphs and pass in selected widgets + date as parameters

        # Close GUI after creation
        self.root.destroy()
        return

    # MM-DD to [MM-DD-YY, MM-DD-YY]
    def convert_date(self):
        date_range = []
        date = ''

        # Day
        if self.date_type.get() == 1:
            date += self.date_text.get()
            date += "-"
            date += self.current_year
            date_range.append(date)
            date_range.append(date)

        # Week
        elif self.date_type.get() == 2:
            date += self.date_text.get()
            date += "-"
            date += self.current_year
            date_range.append(date)
            date = ''

        # Month
        elif self.date_type.get() == 3:
            date += self.date_text.get()
            date += "-"
            date += self.current_year
            date_range.append(date)

        # Year
        elif self.date_type.get() == 4:
            date += self.date_text.get()
            date += "-"
            date += self.current_year
            date_range.append(date)

        return date_range


    # Generate links and call the dashboard
    def generate_graphs(self):
        graph_url = ''


    # Returns list of selected graphs
    def get_graphs(self):
        return self.selected


app = GUI()
