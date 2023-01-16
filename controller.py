from model import Model
from view import View
import tkinter as tk

class Controller: 
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_typing(self, event):
        user_input = self.view.search_var.get()
        self.view.suggestions_list.delete(0, tk.END)
        suggestions = self.model.get_suggestions(user_input)
        for suggestion in suggestions:
            self.view.suggestions_list.insert(tk.END, suggestion)

    def on_select(self, event):
        widget = event.widget
        selection = widget.get(widget.curselection())
        self.view.search_var.set(selection)
        
        self.view.suggestions_list.delete(0, tk.END)

        print(f"You selected: {selection}")
        
if __name__ == "__main__": 
    analyzer = Controller()
    analyzer.main()
