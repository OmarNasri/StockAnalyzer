import tkinter as tk

class View(tk.Tk):
    PAD = 10 # Padding

    def __init__(self, controller): 
        super().__init__()
        self.controller = controller
        self.title("Stock Analyzer")
        self.geometry("500x500")
        self.create_search_bar()

    def main(self):
        self.mainloop()

    def create_search_bar(self):
        stock = tk.Entry(self)
        stock.pack(padx = self.PAD, pady = self.PAD)
        stock.place(x = 150, y = 200, width = 200, height = 20)