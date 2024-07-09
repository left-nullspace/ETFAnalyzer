import pandas as pd
import numpy as np

def calculate_performance(etf_data, starting_capital):
    normalized_data = etf_data / etf_data.iloc[0] * starting_capital
    return normalized_data

def calculate_correlation_matrix(etf_data):
    correlation_matrix = etf_data.pct_change().corr()
    return correlation_matrix.round(2)

def calculate_drawdown(etf_data):
    drawdowns = etf_data / etf_data.cummax() - 1
    return drawdowns

def calculate_annualized_return(etf_data):
    returns = etf_data.pct_change().mean() * 252
    return returns

def calculate_volatility(etf_data):
    volatility = etf_data.pct_change().std() * np.sqrt(252)
    return volatility

def calculate_sharpe_ratio(etf_data, risk_free_rate=0.01):
    annualized_return = calculate_annualized_return(etf_data)
    volatility = calculate_volatility(etf_data)
    sharpe_ratio = (annualized_return - risk_free_rate) / volatility
    return sharpe_ratio
