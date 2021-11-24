import yfinance as yf
import nsepy as ns
import streamlit as st
import pandas as pd
from datetime import datetime

st.write("""
# Simple Strock Price App

Shown Are The Stock **Closing Price** and ***Volume*** of Dillard's, Inc. Price!
""")

#you can always change tickersysmbols
tickerSymbol = 'DDS'     
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker till today
tickerDf = tickerData.history(period ='id', start = '1995-11-30', end = datetime.today().strftime('%Y-%m-%d'))
#open high low close volume dividents stock slits

st.write("""
## Closing Price 
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")

st.line_chart(tickerDf.Volume)