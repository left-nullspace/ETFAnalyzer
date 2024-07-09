import pandas as pd
import yfinance as yf

def get_etf_list():
    # This function returns a dictionary of diverse ETFs with their descriptions
    return {
        "SPY": {"description": "S&P 500 Index Fund - Large-cap U.S. stocks"},
        "QQQ": {"description": "Nasdaq 100 Index Fund - Technology-focused U.S. stocks"},
        "VTI": {"description": "Total Stock Market Index Fund - Broad U.S. stock market"},
        "EFA": {"description": "iShares MSCI EAFE ETF - Developed international stocks"},
        "EEM": {"description": "iShares MSCI Emerging Markets ETF - Emerging markets stocks"},
        "AGG": {"description": "iShares Core U.S. Aggregate Bond ETF - Broad U.S. bond market"},
        "LQD": {"description": "iShares iBoxx $ Investment Grade Corporate Bond ETF - Investment-grade corporate bonds"},
        "HYG": {"description": "iShares iBoxx $ High Yield Corporate Bond ETF - High yield corporate bonds"},
        "TLT": {"description": "iShares 20+ Year Treasury Bond ETF - Long-term U.S. Treasury bonds"},
        "TIP": {"description": "iShares TIPS Bond ETF - U.S. Treasury Inflation-Protected Securities"},
        "GLD": {"description": "SPDR Gold Shares - Gold bullion"},
        "SLV": {"description": "iShares Silver Trust - Silver bullion"},
        "VNQ": {"description": "Vanguard Real Estate ETF - U.S. REITs"},
        "VEU": {"description": "Vanguard FTSE All-World ex-US ETF - International stocks excluding U.S."},
        "VTIP": {"description": "Vanguard Short-Term Inflation-Protected Securities ETF - Short-term TIPS"},
        "BND": {"description": "Vanguard Total Bond Market ETF - Broad U.S. bond market"},
        "BNDX": {"description": "Vanguard Total International Bond ETF - Broad international bond market"},
        "XLE": {"description": "Energy Select Sector SPDR Fund - U.S. energy sector"},
        "XLK": {"description": "Technology Select Sector SPDR Fund - U.S. technology sector"},
        "XLF": {"description": "Financial Select Sector SPDR Fund - U.S. financial sector"},
        "XLV": {"description": "Health Care Select Sector SPDR Fund - U.S. healthcare sector"},
        "XLY": {"description": "Consumer Discretionary Select Sector SPDR Fund - U.S. consumer discretionary sector"},
        "XLP": {"description": "Consumer Staples Select Sector SPDR Fund - U.S. consumer staples sector"},
    }


def load_etf_data(etf_list, start_date, end_date):
    etf_data = {}
    for etf in etf_list:
        data = yf.download(etf, start=start_date, end=end_date)
        etf_data[etf] = data['Adj Close']
    return pd.DataFrame(etf_data)
