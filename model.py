import requests
import config

class Model: 
    def __init__(self):
        pass

    def get_stock_data(self):
        url = "https://fcsapi.com/api-v3/stock/list?country=Finland&access_key=" + config.stockDataApiKey
        response = requests.get(url)
        data = response.json()
        return data
