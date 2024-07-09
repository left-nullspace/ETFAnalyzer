import streamlit as st
from data_loader import load_etf_data, get_etf_list
from analysis import calculate_performance, calculate_correlation_matrix, calculate_drawdown, calculate_annualized_return, calculate_volatility, calculate_sharpe_ratio
from visualization import plot_performance, plot_correlation_matrix, plot_drawdown
import pandas as pd
import datetime

# Title and description
st.title("Interactive ETF Analysis Tool")

# Sidebar for inputs
st.sidebar.header("ETF Selection and Inputs")

# ETF selection
etf_list = get_etf_list()
selected_etfs = st.sidebar.multiselect(
    "Select ETFs to Analyze",
    options=etf_list.keys(),
    format_func=lambda x: f"{x} - {etf_list[x]['description']}",
)

# Starting capital and date range
starting_capital = st.sidebar.number_input("Enter Starting Capital", value=10000)
min_date = datetime.date(2000, 1, 1)  # Set a reasonable minimum date
max_date = datetime.date.today()  # Set the maximum date to today
start_date = st.sidebar.date_input("Select Start Date", value=min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Select End Date", value=max_date, min_value=min_date, max_value=max_date)

# Button to trigger analysis
if st.sidebar.button("Run Analysis"):
    if selected_etfs and start_date and end_date:
        etf_data = load_etf_data(selected_etfs, start_date, end_date)

        # Performance analysis
        performance_data = calculate_performance(etf_data, starting_capital)
        st.subheader("Performance of Selected ETFs")
        st.plotly_chart(plot_performance(performance_data))

        # Drawdown analysis
        drawdown_data = calculate_drawdown(etf_data)
        st.subheader("Drawdown Analysis")
        st.plotly_chart(plot_drawdown(drawdown_data))

        # Correlation matrix
        correlation_matrix = calculate_correlation_matrix(etf_data)
        st.subheader("Correlation Matrix")
        st.plotly_chart(plot_correlation_matrix(correlation_matrix))

        # Summary statistics
        st.subheader("Summary Statistics")
        summary_stats = pd.DataFrame({
            "Annualized Return (%)": calculate_annualized_return(etf_data) * 100,
            "Volatility (%)": calculate_volatility(etf_data) * 100,
            "Max Drawdown (%)": drawdown_data.min() * 100,
            "Sharpe Ratio": calculate_sharpe_ratio(etf_data)
        })
        st.write(summary_stats)
    else:
        st.error("Please select at least one ETF and specify a valid date range.")

# Footer
st.text("Created by Alan")
st.text("Investing involves risk. Past performance is not indicative of future results.")
