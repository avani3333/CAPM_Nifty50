import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import function

st.set_page_config(page_title="CAPM for Nifty 50",
                   page_icon="chart_with_upwards_trend",
                   layout="wide")

st.title("Capital Asset Pricing Model for Nifty 50")

col1, col2 = st.columns([1, 1])
with col1:
    nifty50_stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS', 'HINDUNILVR.NS', 'KOTAKBANK.NS', 'HDFC.NS', 'LT.NS', 'SBIN.NS']
    stocks_list = st.multiselect("Choose 4 stocks", nifty50_stocks, nifty50_stocks[:4])
with col2:
    year = st.number_input("Number of Years", 1, 10)

try:
    end = datetime.date.today()
    start = datetime.date(end.year - year, end.month, end.day)

    # Attempt to fetch Nifty 50 index data using different possible symbols
    try:
        nifty50 = yf.download('^NSEI', start=start, end=end)
    except KeyError:
        try:
            nifty50 = yf.download('^NSE', start=start, end=end)
        except KeyError:
            nifty50 = yf.download('NSEI', start=start, end=end)

    nifty50.reset_index(inplace=True)
    nifty50 = nifty50[['Date', 'Close']]
    nifty50.columns = ['Date', 'nifty50']
    nifty50['Date'] = pd.to_datetime(nifty50['Date'])

    # Initialize an empty DataFrame to hold all stocks' data
    all_stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock, start=start, end=end)
        data.reset_index(inplace=True)
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            stock_df = data[['Date', 'Close']].rename(columns={'Close': stock})
            if all_stocks_df.empty:
                all_stocks_df = stock_df
            else:
                all_stocks_df = pd.merge(all_stocks_df, stock_df, on='Date', how='outer')
        else:
            st.warning(f"Data for {stock} does not contain a 'Date' column and was not included.")

    if all_stocks_df.empty or 'Date' not in all_stocks_df.columns:
        st.error("No valid stock data found or 'Date' column missing.")
        st.stop()

    # Set 'Date' as the index for both DataFrames
    all_stocks_df.set_index('Date', inplace=True)
    nifty50.set_index('Date', inplace=True)

    # Merge all_stocks_df and nifty50 on 'Date'
    merged_df = pd.merge(all_stocks_df, nifty50, left_index=True, right_index=True, how='inner')

    # Display DataFrame head and tail
    co1, co2 = st.columns([1, 1])
    with co1:
        st.markdown("### Dataframe head")
        st.dataframe(merged_df.head(), use_container_width=True)
    with co2:
        st.markdown("### Dataframe tail")
        st.dataframe(merged_df.tail(), use_container_width=True)

    # Plot the data using the function from function.py
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Price of all Stocks")
        st.plotly_chart(function.interactive_plot(merged_df))

    # Normalize the merged_df for plotting normalized data
    normalized_df = function.normalize(merged_df)

    # Plot normalized data
    with col2:
        st.markdown("### Price of all Stocks after Normalization")
        st.plotly_chart(function.interactive_plot(normalized_df))

    # Calculate daily returns
    stocks_daily_return = function.daily_return(normalized_df)

    beta = {}
    alpha = {}

    for stock in stocks_daily_return.columns:
        if stock != 'Date' and stock != 'nifty50':
            b, a = function.calc_beta(stocks_daily_return, stock)
            beta[stock] = b
            alpha[stock] = a

    beta_df = pd.DataFrame(list(beta.items()), columns=['Stock', 'Beta Value'])
    beta_df['Beta Value'] = beta_df['Beta Value'].round(2)

    with col1:
        st.markdown("### Calculated Beta Value")
        st.dataframe(beta_df, use_container_width=True)

    # Assuming risk-free rate (rf) is 0% for simplicity
    rf = 0
    # Annualized market return based on Nifty 50 index
    rm = stocks_daily_return['nifty50'].mean() * 252

    return_df = pd.DataFrame(columns=['Stock', 'Return Value'])
    return_df['Stock'] = stocks_list
    return_value = [str(round(rf + (beta[stock] * (rm - rf)), 2)) for stock in stocks_list if stock in beta]
    return_df['Return Value'] = return_value

    with col2:
        st.markdown("### Calculated Return using CAPM")
        st.dataframe(return_df, use_container_width=True)
except Exception as e:
    st.write("An error occurred:", e)
