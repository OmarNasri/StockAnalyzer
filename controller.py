from model import Model
from view import View
import tkinter as tk

class Controller: 
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def main(self):
        self.view.main()

    def get_current_price(self):
        price = self.model.show_current_price("AAPL")
        return price
        
    def get_predicted_price(self):
        prediction = self.model.analyze("AAPL")
        self.plot_predicted_data(prediction[1], prediction[2])
        prediction = prediction[0]
        prediction = str(prediction)
        prediction = prediction[2:-2]
        return prediction
    
    def plot_predicted_data(self, actual,prediction):
        self.view.ax.clear()
        self.view.ax.plot(prediction, label='Predicted Prices', color='red')
        self.view.ax.plot(actual, label='Actual Prices', color='blue')
        self.view.ax.set_xlabel('Time')
        self.view.ax.set_ylabel('Price')
        self.view.ax.legend(loc='best')
        self.view.canvas.draw()
    
    # Event handlers
    def on_typing(self, event):
        user_input = self.view.search_var.get()
        self.view.suggestions_list.delete(0, tk.END)
        suggestions = self.model.get_suggestions(user_input)
        for suggestion in suggestions:
            self.view.suggestions_list.insert(tk.END, suggestion)

    def on_select(self, event):
        widget = event.widget
        selection = widget.get(widget.curselection())
        self.view.search_bar.delete(0, tk.END)
        self.view.suggestions_list.delete(0, tk.END)
        self.view.chosen_stock.config(text=selection)
    
    
    def on_click(self):
        self.view.predicted_price.config(text="Predicted price for tomorrow: " + self.get_predicted_price())
        
       
       
       
if __name__ == "__main__": 
    analyzer = Controller()
    analyzer.main()
   