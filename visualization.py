import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def plot_performance(performance_data):
    fig = go.Figure()
    for column in performance_data.columns:
        fig.add_trace(go.Scatter(x=performance_data.index, y=performance_data[column], mode='lines', name=column))
    fig.update_layout(title='Performance of Selected ETFs', xaxis_title='Date', yaxis_title='Value')
    return fig

def plot_correlation_matrix(correlation_matrix):
    fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto")
    fig.update_layout(title='Correlation Matrix', xaxis_title='ETFs', yaxis_title='ETFs')
    return fig

def plot_drawdown(drawdown_data):
    fig = go.Figure()
    for column in drawdown_data.columns:
        fig.add_trace(go.Scatter(x=drawdown_data.index, y=drawdown_data[column], mode='lines', name=column))
    fig.update_layout(title='Drawdown Analysis', xaxis_title='Date', yaxis_title='Drawdown')
    return fig

def display_summary_statistics(summary_statistics):
    st.table(summary_statistics.style.format({
        'Average Annual % Gain': '{:.2f}%',
        'Average Annual Std Dev': '{:.2f}%',
        'Annual Sharpe Ratio': '{:.2f}'
    }).background_gradient(cmap='viridis'))
