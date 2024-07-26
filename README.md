# CAPM Analysis for Nifty 50 Stocks📈
This project provides a Capital Asset Pricing Model (CAPM) analysis for stocks within the Nifty 50 index. It includes features for visualizing stock prices, calculating normalized returns, and determining the beta value and expected return using the CAPM formula.

## 🔗 Project Link
https://capm-nifty50.streamlit.app/
## 


## Screenshots

![Screenshot 2024-07-26 145851](https://github.com/user-attachments/assets/a809772c-d38d-46d1-87e4-997e61b07af4)


### Features
● **Stock Price Visualization:** Interactive line charts showing historical prices of selected Nifty 50 stocks.

● **Normalization:** Comparison of stock performance by normalizing prices.

● **Beta Calculation:** Calculation of beta values for stocks relative to the Nifty 50 index.

● **Expected Return Calculation:** Estimation of expected returns using the CAPM formula.

## Price of all Stocks

![Screenshot 2024-07-26 150258](https://github.com/user-attachments/assets/5391aef4-9a67-4209-bac5-8cabcb13c00b)


### Setup

**Install Required Packages:**
Use pip to install the required Python packages.

pip install -r requirements.txt


**Select Stocks and Time Frame:**

● Choose up to 4 Nifty 50 stocks to analyze.

● Specify the number of years for historical data.

**View Analysis:**

●**Stock Prices:** See the price history of selected stocks.

●**Normalized Prices:** Compare the normalized performance of the stocks.

●**Beta Values:** View the beta values calculated relative to the Nifty 50 index.

●**Expected Returns:** Check the expected returns calculated using the CAPM formula.

## Price of all stocks after Normalization

![Screenshot 2024-07-26 150453](https://github.com/user-attachments/assets/e4dcb142-0cd1-4d56-b575-208a99a3b7e3)


## Project Structure

● **return.py:** The main script for running the Streamlit application.

● **function.py:** Contains the core functions for data fetching, processing, and calculation:

    ●interactive_plot(df): Generates interactive plots for stock data.
    ●normalize(df): Normalizes stock prices.
    ●daily_return(df): Calculates daily returns.
    ●calc_beta(df, stock): Calculates the beta value for a stock.
● **requirements.txt:** A list of required Python packages.

## Calculated Beta Value

![Screenshot 2024-07-26 150634](https://github.com/user-attachments/assets/76e4463d-9932-42f0-b34f-00c36611b613)


## Calculated Return using CAPM

![Screenshot 2024-07-26 150722](https://github.com/user-attachments/assets/b4e0de11-9baf-4fae-9306-b85c86d7281e)


### Data Source
The data for Nifty 50 and its constituent stocks is fetched using the yfinance library, which sources data from Yahoo Finance.






## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.datascienceportfol.io/avani)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](http://linkedin.com/in/avani-choudhary13)


