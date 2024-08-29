import streamlit as st
import yfinance as yf
import datetime

ticker_symbol = st.text_input("Enter the Stock Name", "AAPL")

col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("START DATE",value=datetime.date(2019,7,1))

with col2:
    end_date = st.date_input("END DATE",value=datetime.date(2023,7,1))

data = yf.download(ticker_symbol,start=start_date,end=end_date)

st.write(data)
st.line_chart(data["Close"])


