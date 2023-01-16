import requests
import config
import json 

class Model: 
    def __init__(self):
        #url = "https://fcsapi.com/api-v3/stock/list?country=Finland&access_key=" + config.stockDataApiKey
        #response = requests.get(url)
        #self.data = response.json()
        with open ("C:\\Users\\omarn\\stocks.txt", "r") as f:
            response = json.load(f)
        self.data = response
        self.names = []
        for item in self.data.get("response"):
            self.names.append(item.get("name"))
        self.names.sort()

    def get_suggestions(self, user_input):
        suggestions = []
        for item in self.names:
            if user_input.casefold() in item.casefold():
                suggestions.append(item)
        return suggestions

    