from model import Model
from view import View

class Controller: 
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        #self.view.main()
        print(self.model.get_stock_data())

if __name__ == "__main__": 
    analyzer = Controller()
    analyzer.main()
