from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        print("\n-----------------| GUI |-----------------\n")

        # Generate window
        self.root = Tk()
        self.root.title("Generate Graphs")
        self.root.maxsize(160, 400)
        self.root.minsize(160, 400)

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
        self.graph_label = Label(self.root, text="Graph selection:", pady=10).pack(anchor=W)
        self.graph_0 = ttk.Checkbutton(self.root, text="Employee information", variable=self.a, width=200, style="TCheckbutton").pack(anchor=W)
        self.graph_1 = ttk.Checkbutton(self.root, text="# of customers per hour", variable=self.b, width=200).pack(anchor=W)
        self.graph_2 = ttk.Checkbutton(self.root, text="Daily customer statistics", variable=self.c, width=200).pack(anchor=W)
        self.graph_3 = ttk.Checkbutton(self.root, text="Revenue", variable=self.d, width=200).pack(anchor=W)
        self.graph_4 = ttk.Checkbutton(self.root, text="Items sold", variable=self.e, width=200).pack(anchor=W)
        self.graph_5 = ttk.Checkbutton(self.root, text="Extra statistics", variable=self.f, width=200).pack(anchor=W)

        # Radiobuttons
        self.radio_label = Label(self.root, text="Data of graph(s)", pady=10).pack(anchor=W)
        self.daily_button = ttk.Radiobutton(self.root, text="Day", variable=self.date_type, value = 1).pack(anchor=W)
        self.weekly_button = ttk.Radiobutton(self.root, text="Week", variable=self.date_type, value = 2).pack(anchor=W)
        self.monthly_button = ttk.Radiobutton(self.root, text="Month", variable=self.date_type, value = 3).pack(anchor=W)
        self.year_button = ttk.Radiobutton(self.root, text="Current year", variable=self.date_type, value = 4).pack(anchor=W)

        # Entry
        self.date_label = Label(self.root, text="Date (MM-DD):", pady=10).pack(anchor=W)
        self.date_entry = ttk.Entry(self.root, textvariable=self.date_text).pack(anchor=W)

        # Blank label
        self.empty_label = Label(self.root, text="").pack(anchor=W)

        # Create button
        self.display = ttk.Button(self.root, text="Create", style="TButton", command=self.generate_graphs).pack(anchor=W)
        #self.display = Button(self.frame, text="Generate", command=self.generate_graphs).pack(anchor=W)

        print("> Successfully created GUI")
        print("> Waiting for input")

        self.root.mainloop()


    def generate_graphs(self):
        print("> The following graphs were selected: ", end='')
        for graph in range(6):
            if self.graphs[graph].get():
                self.selected.append(graph)
                print(graph, end=' ')
        print("\n> Generating graphs, please wait")

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

        #TODO: Call dataAnalysis on selected graphs and pass in selected widgets + date as parameters

        # Close GUI after creation
        self.root.destroy()

    # Returns list of selected graphs
    def get_graphs(self):
        return self.selected

# app = GUI()
