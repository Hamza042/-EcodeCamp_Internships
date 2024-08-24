
# Create your views here.
# stockanalysis/views.py

import pandas as pd
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from .forms import StockForm

def stock_analysis(request):
    form = StockForm(request.POST or None)
    plot_url = None
    error = None

    if form.is_valid():
        ticker = form.cleaned_data['ticker']
        horizon_days = int(form.cleaned_data['horizon'])
        
        # Fetch data from Yahoo Finance
        df = yf.download(ticker, start="2009-01-01", end="2023-01-01")
        
        if df.empty:
            error = 'Invalid ticker symbol'
        else:
            df = df.reset_index()
            df = df.drop(['Date', 'Adj Close'], axis=1, errors='ignore')
            df = df.rename(columns={'Close': 'Price'})
            
            # Moving Averages
            ma100 = df['Price'].rolling(100).mean()
            ma200 = df['Price'].rolling(200).mean()

            # Prepare Data for Model
            train_df = df['Price'][:int(len(df) * 0.80)]
            test_df = df['Price'][int(len(df) * 0.80):]

            scaler = MinMaxScaler(feature_range=(0, 1))
            train_df_arr = scaler.fit_transform(train_df.values.reshape(-1, 1))

            x_train, y_train = [], []
            for i in range(100, len(train_df_arr)):
                x_train.append(train_df_arr[i-100:i])
                y_train.append(train_df_arr[i, 0])
            x_train, y_train = np.array(x_train), np.array(y_train)

            # Build and Train Model
            model = Sequential()
            model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(x_train.shape[1], 1)))
            model.add(Dropout(0.2))
            model.add(LSTM(units=60, activation='relu', return_sequences=True))
            model.add(Dropout(0.3))
            model.add(LSTM(units=80, activation='relu', return_sequences=True))
            model.add(Dropout(0.4))
            model.add(LSTM(units=120, activation='relu'))
            model.add(Dropout(0.5))
            model.add(Dense(units=1))
            model.compile(loss='mean_squared_error', optimizer='adam')
            model.fit(x_train, y_train, epochs=50, verbose=0)

            # Prepare test data and make predictions
            past_100_days = train_df.tail(100)
            final_df = pd.concat([past_100_days, test_df], ignore_index=True)
            input_data = scaler.transform(final_df.values.reshape(-1, 1))
            
            x_test, y_test = [], []
            for i in range(100, len(input_data)):
                x_test.append(input_data[i-100:i])
                y_test.append(input_data[i, 0])
            x_test, y_test = np.array(x_test), np.array(y_test)
            
            y_pred = model.predict(x_test)
            scale = scaler.scale_
            scale_factor = 1 / scale
            y_pred = y_pred * scale_factor
            y_test = y_test * scale_factor

            # Plot results
            plt.figure(figsize=(12, 6))
            plt.plot(y_test, 'g', label="Original Price")
            plt.plot(y_pred, 'r', label="Predicted Price")
            plt.xlabel("Time")
            plt.ylabel("Price [ $ ]")
            plt.title(f"{ticker} Stock Price Prediction")
            plt.legend()

            # Save plot to a BytesIO object
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()

    return render(request, 'stockanalysis/stock_analysis.html', {'form': form, 'plot_url': plot_url, 'error': error})
