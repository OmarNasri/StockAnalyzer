import tkinter as tk
import json 


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Stock Analyzer")
        self.search_var = tk.StringVar()
        self.search_bar = tk.Entry(self, textvariable=self.search_var)
        self.search_bar_label = tk.Label(self, text="Search for a stock:")
        self.search_bar_label.pack(pady=10, padx=10)
        self.search_bar.pack(pady=0, padx=10)
        self.search_bar.bind("<Key>", self.controller.on_typing)
        self.suggestions_list = tk.Listbox(self)
        self.suggestions_list.pack(pady=10)
        self.suggestions_list.bind("<<ListboxSelect>>", self.controller.on_select)
        #create start date entry
        self.s_date = tk.StringVar()
        self.start_date = tk.Entry(self, textvariable=self.s_date)
        #place start date entry under search bar
        self.start_date.pack(pady=10)

    def main(self):
        self.mainloop()
