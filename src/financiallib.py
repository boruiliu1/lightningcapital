import yfinance as yf

data = yf.download("AAPL", start="2024-01-01", end="2025-01-02")
print(data)
