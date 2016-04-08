from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        print("\n-----------------| GUI |-----------------\n")

        # Generate window
        self.root = Tk()
        self.root.title("Generate Graphs")
        self.frame = Frame(self.root)
        self.root.maxsize(250, 180)
        self.root.minsize(250, 180)

        # ttk styles
        self.green_button = ttk.Style()
        self.green_button.map("TButton", foreground=[('pressed', 'white'), ('active', 'green')],  background=[('pressed', 'white'), ('active', 'white')])

        # Checkbutton variables
        self.a = IntVar()
        self.b = IntVar()
        self.c = IntVar()
        self.d = IntVar()
        self.e = IntVar()
        self.f = IntVar()
        self.graphs = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.selected = []

        # Checkbuttons
        self.graph_0 = ttk.Checkbutton(self.root, text="Employee information", variable=self.a, width=200, style="TCheckbutton")
        self.graph_0.pack()
        self.graph_1 = ttk.Checkbutton(self.root, text="Number of customers per hour", variable=self.b, width=200)
        self.graph_1.pack()
        self.graph_2 = ttk.Checkbutton(self.root, text="Daily customer statistics (multigraph)", variable=self.c, width=200)
        self.graph_2.pack()
        self.graph_3 = ttk.Checkbutton(self.root, text="Revenue (daily, monthly, yearly)", variable=self.d, width=200)
        self.graph_3.pack()
        self.graph_4 = ttk.Checkbutton(self.root, text="Items sold (daily, monthly, yearly)", variable=self.e, width=200)
        self.graph_4.pack()
        self.graph_5 = ttk.Checkbutton(self.root, text="Extra statistics", variable=self.f, width=200)
        self.graph_5.pack()

        # Blank label
        self.empty_label = Label(self.root, text="")
        self.empty_label.pack()

        # Create button
        self.display = ttk.Button(self.frame, text="Create", style="TButton", command=self.generate_graphs)
        self.display.pack()

        # Finalize window
        self.frame.pack()

        print("> Successfully created GUI")
        print("> Waiting for input")

        # Wait for input
        self.frame.mainloop()


    def generate_graphs(self):
        print("The following graphs were selected: ", end='')
        for graph in range(6):
            if self.graphs[graph].get():
                self.selected.append(graph)
                print(graph, end=' ')
        self.frame.mainloop()


    # Returns list of selected graphs
    def get_graphs(self):
        return self.selected
