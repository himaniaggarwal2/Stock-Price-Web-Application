import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Boeing Company!
""")
        
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'BA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""# Stock Price""")
st.line_chart(tickerDf.Close)

st.write("""# Volume""")
st.line_chart(tickerDf.Volume)

st.write("""# Calendar""")
tickerData.calendar


st.write("""# Broker Recommendations""")
#get recommendation data for ticker
tickerData.recommendations

st.write("""# Company Info.""")
#info on the company
tickerData.info
