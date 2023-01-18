import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import yfinance as yfin


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Stock Analyzer")
        self.geometry("800x800")

        self.search_label = tk.Label(self, text="Search for a stock:")
        self.search_label.grid(row=0, column=0, padx=10, pady=0,sticky="W")
        self.search_var = tk.StringVar()
        self.search_bar = tk.Entry(self, textvariable=self.search_var)
        self.search_bar.grid(row=0, column=1, padx=10, pady=7,sticky="E")
        self.search_bar.bind("<Key>", self.controller.on_typing)

        self.suggestions_list_label = tk.Label(self, text="Choose your stock:")
        self.suggestions_list_label.grid(row=2, column=0, padx=10, pady=10,sticky="W")
        self.suggestions_list = tk.Listbox(self)
        self.suggestions_list.grid(row=2, column=1, padx=10, pady=10,sticky="E")
        self.suggestions_list.bind("<<ListboxSelect>>", self.controller.on_select)

        self.chosen_stock_label = tk.Label(self, text="Chosen stock:")
        self.chosen_stock_label.grid(row=3, column=0, padx=10, pady=10,sticky="W")
        self.chosen_stock = tk.Label(self, text="")
        self.chosen_stock.grid(row=3, column=1, padx=10, pady=10,sticky="E")

    
        self.current_price_label = tk.Label(self, text="Current price:")
        self.current_price_label.grid(row=4, column=0, padx=10, pady=10,sticky="W")
        self.current_price = tk.Label(self, text=self.controller.get_current_price())
        self.current_price.grid(row=4, column=1, padx=10, pady=10,sticky="E")


        self.predict_price_button = tk.Button(self, text="Predict price for tomorrow", command=self.controller.on_click)
        self.predict_price_button.grid(row=5, column=0, padx=10, pady=10,sticky="W")

        self.predicted_price = tk.Label(self, text="")
        self.predicted_price.grid(row=6, column=0, padx=10, pady=10,sticky="E")

        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

         
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=7, column=0, padx=10, pady=10,sticky="W")

    def main(self):
        self.mainloop()

    
