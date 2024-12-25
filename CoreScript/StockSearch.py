import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

class StockDataGenerator:
    def __init__(self, output_dir="_posts"):
        """Initialize the stock data generator."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def get_stock_data(self, symbol, period="1mo"):
        """
        Fetch stock data from Yahoo Finance.
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL')
            period (str): Time period (e.g., '1mo', '1y', '5y')
        """
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        info = stock.info
        return hist, info

    def create_markdown_post(self, symbol):
        """Generate a markdown post for the given stock symbol."""
        try:
            hist, info = self.get_stock_data(symbol)
            
            # Format the date for the filename and front matter
            current_date = datetime.now().strftime('%Y-%m-%d')
            
            # Create the filename
            filename = f"{current_date}-{symbol.lower()}-analysis.md"
            filepath = os.path.join(self.output_dir, filename)
            
            # Prepare the content
            content = f"""---
title: "{symbol} Stock Analysis"
date: {current_date}
categories:
  - Stock Analysis
tags:
  - {symbol}
  - Market Analysis
---

## {symbol} Stock Analysis

### Company Overview
- **Company Name:** {info.get('longName', 'N/A')}
- **Industry:** {info.get('industry', 'N/A')}
- **Sector:** {info.get('sector', 'N/A')}
- **Current Price:** ${info.get('currentPrice', 'N/A')}
- **Market Cap:** ${info.get('marketCap', 'N/A'):,.2f}

### Recent Performance
"""
