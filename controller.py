from model import Model
from view import View
import tkinter as tk
import numpy as np


class Controller: 
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.company = ""
        self.ticker = ""
    
    def main(self):
        self.view.main()

    def get_current_price(self,ticker):
        price = self.model.show_current_price(ticker)
        return price
        
    def get_predicted_price(self,ticker):
        prediction = self.model.analyze(ticker)
        prediction = str(prediction)
        prediction = prediction[2:-2]
        self.plot_predicted_data()
        return prediction
    
    def plot_predicted_data(self):
        self.view.ax.clear()
        predictedPrices = self.model.getPredictedPrices()
        actualPrices = self.model.getActualPrices()
        self.view.ax.plot(predictedPrices, label='Predicted Prices', color='red')
        self.view.ax.plot(actualPrices, label='Actual Prices', color='blue')
        self.view.ax.set_xlabel('Time')
        self.view.ax.set_ylabel('Price')
        self.view.ax.legend(loc='best')
        self.view.canvas.draw()
    
    # Event handlers
    def on_typing(self,event):
        user_input = self.view.search_var.get()
        self.view.suggestions_list.delete(0, tk.END)
        suggestions = self.model.get_suggestions(user_input)
        for suggestion in suggestions:
            self.view.suggestions_list.insert(tk.END, suggestion)

    def on_select(self, event):
        widget = event.widget
        self.company = widget.get(widget.curselection())
        self.view.search_bar.delete(0, tk.END)
        self.view.suggestions_list.delete(0, tk.END)
        try: 
            self.view.predicted_price.config(text="")
            self.view.chosen_stock.config(text="Chosen stock: " +self.company)
            self.ticker = self.model.get_ticker(self.company)
            self.view.current_price.config(text="Current price: " + self.get_current_price(self.ticker))
        except:
            self.view.current_price.config(text="")
            self.view.chosen_stock.config(text="ERROR: Stock data not found. Try another stock.")
    
    
    # Todo: Add analyzing status
    def on_click(self):
        try:
            self.view.predicted_price.config(text="Analyzing...")
            self.view.after(2000, lambda:
            self.view.predicted_price.config(text="Predicted price for tomorrow: " + self.get_predicted_price(self.ticker)))
        except:
            self.view.predicted_price.config(text="ERROR: No stock chosen")
       
       
if __name__ == "__main__": 
    analyzer = Controller()
    analyzer.main()