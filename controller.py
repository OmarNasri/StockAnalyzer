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
        prediction = str(prediction)
        prediction = prediction[2:-2]
        
        return prediction
    
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
    
    #create event handler for the button to update the predicted_price text
    def on_click(self):
        self.view.predicted_price.config(text="Predicted price for tomorrow: " + self.get_predicted_price())
       
if __name__ == "__main__": 
    analyzer = Controller()
    analyzer.main()
