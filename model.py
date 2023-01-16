import requests
import config
import json 

class Model: 
    def __init__(self):
        #url = "https://fcsapi.com/api-v3/stock/list?country=Finland&access_key=" + config.stockDataApiKey
        #response = requests.get(url)
        with open ("C:\\Users\\omarn\\stocks.txt", "r") as f:
        #load data from file into response variable
            response = json.load(f)
        #self.data = response.json()
        self.data = response
        self.names = []
        for item in self.data.get("response"):
            self.names.append(item.get("name"))
        self.names.sort()

    def get_suggestions(self, user_input):
        suggestions = []
        for item in self.names:
            if user_input in item.casefold():
                suggestions.append(item)
        return suggestions

    