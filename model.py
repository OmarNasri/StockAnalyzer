import requests
from datetime import date
import config
import json 
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import yfinance as yfin
from tensorflow.keras.layers import Dense, Dropout, LSTM
yfin.pdr_override()

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

    def show_current_price(self,company):
        ticker = yfin.Ticker(company).info
        market_price = ticker['regularMarketPrice']
        return market_price

    def analyze(self,company):
        start = "2015-01-01"
        end = "2022-01-01"

        data = pdr.get_data_yahoo(company,start= start, end= end)

        #Prepare data
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))
        prediction_days = 30
        x_train = []
        y_train = []
        for x in range(prediction_days, len(scaled_data)):
            x_train.append(scaled_data[x-prediction_days:x, 0])
            y_train.append(scaled_data[x, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        #Create the model
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1)) 
        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_train, y_train, epochs=25, batch_size=32)
      

        #Test the model accuracy on existing data
    
        test_start = "2020-01-01"
        test_end = date.today().strftime("%Y-%m-%d")
        test_data = pdr.get_data_yahoo(company,start= test_start, end= test_end)
        actual_prices = test_data['Close'].values
        total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)
        model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
        model_inputs = model_inputs.reshape(-1,1)
        model_inputs = scaler.transform(model_inputs)

        #Make predictions on test data
        x_test = []
        for x in range(prediction_days, len(model_inputs)):
            x_test.append(model_inputs[x-prediction_days:x, 0])
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        predicted_prices = model.predict(x_test)
        predicted_prices = scaler.inverse_transform(predicted_prices)

        #Plot the test predictions
        plt.plot(actual_prices, color="black", label=f"Actual {company} Price")
        plt.plot(predicted_prices, color="green", label=f"Predicted {company} Price")
        plt.title(f"{company} Share Price")
        plt.xlabel('Time')
        plt.ylabel(f"{company} Share Price")
        plt.legend()
        plt.show(block=False)
        
        
        
        #Predict next day  
        real_data = [model_inputs[len(model_inputs)+1-prediction_days:len(model_inputs+1), 0]]
        real_data = np.array(real_data)
        real_data=np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))

        prediction=model.predict(real_data)
        prediction = scaler.inverse_transform(prediction)
        print(f"Prediction: {prediction}")
        return prediction
    