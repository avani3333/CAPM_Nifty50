import plotly.express as px
import numpy as np

def interactive_plot(df):
    fig = px.line()
    # Determine the date series
    date_series = df['Date'] if 'Date' in df.columns else df.index
    
    for column in df.columns:
        if column != 'Date':  # Avoid plotting the 'Date' column itself
            fig.add_scatter(x=date_series, y=df[column], mode='lines', name=column)
    
    fig.update_layout(
        width=450,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def normalize(df):
    normalized_df = df.copy()
    for column in normalized_df.columns:
        if column != 'Date':  # Skip non-numeric columns like 'Date'
            initial_value = normalized_df[column].iloc[0]
            normalized_df[column] = normalized_df[column] / initial_value
    return normalized_df

def daily_return(df):
    df_daily_return = df.copy()
    for column in df.columns:
        if column != 'Date':  # Calculate returns for numeric columns only
            df_daily_return[column] = df[column].pct_change() * 100
    df_daily_return.fillna(0, inplace=True)  # Set NaN values (e.g., first row) to 0
    return df_daily_return

def calc_beta(stocks_daily_return, stock):
    # Mean of daily returns of the Nifty 50 index multiplied by trading days
    rm = stocks_daily_return['nifty50'].mean() * 252

    # Slope and intercept (beta and alpha) of the line of best fit
    b, a = np.polyfit(stocks_daily_return['nifty50'], stocks_daily_return[stock], 1)
    return b, a
