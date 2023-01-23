
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Stock Analyzer")
        self.geometry("680x1030")
        self.resizable(False, False)
        self.grid_columnconfigure(4, minsize=10)
        
        self.search_label = tk.Label(self, text="Search for a stock:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")
        self.search_var = tk.StringVar()
        self.search_bar = tk.Entry(self,textvariable=self.search_var)
        self.search_bar.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
        self.search_bar.bind("<Key>", self.controller.on_typing)

        self.suggestions_list_label = tk.Label(self, text="Choose your stock:")
        self.suggestions_list_label.grid(row=3, column=0, padx=10, pady=10,sticky="nsew")
        self.suggestions_list = tk.Listbox(self)
        self.suggestions_list.grid(row=4, column=0, padx=10, pady=10,sticky="nsew")
        self.suggestions_list.bind("<<ListboxSelect>>", self.controller.on_select)

        self.chosen_stock = tk.Label(self, text="Chosen stock: ")
        self.chosen_stock.grid(row=5, column=0, padx=10, pady=10,sticky="nsew")


        self.current_price = tk.Label(self, text="Current price: ")
        self.current_price.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        
        self.predict_price_button = tk.Button(self, text="Predict price for tomorrow", command=self.controller.on_click)
        self.predict_price_button.grid(row=7, column=0, padx=10, pady=10,sticky="nsew")

        self.predicted_price = tk.Label(self, text="")
        self.predicted_price.grid(row=8, column=0, padx=10, pady=10,sticky="nsew")

        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=9, column=0, padx=10, pady=10,sticky="W")

        #create exit button and kill the program completely
        self.exit_button = tk.Button(self, text="Exit", command=lambda:sys.exit())
        self.exit_button.grid(row=10, column=0, padx=10, pady=10,sticky="nsew")
        
    def main(self):
        self.mainloop()