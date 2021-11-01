#!/bin/bash/python
#
# file: 1-backtest-sol.py
# abstract: solution for 1-backtest.md
#

import sys
import httpx
from tda.auth import easy_client
from tda.client import Client
from datetime import datetime

c = easy_client(
        api_key=str(sys.argv[1]),
        redirect_uri='https://localhost',
        token_path='./token')

# tickers = ["APPL", "GME", "GOOG"]
tickers = ["APPL"]

for item in tickers:
        
        resp = c.get_price_history('AAPL',
                period_type=Client.PriceHistory.PeriodType.DAY,
                period=Client.PriceHistory.Period.ONE_DAY,
                frequency_type=Client.PriceHistory.FrequencyType.MINUTE,
                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                start_datetime=datetime.fromtimestamp(1635426000),
                end_datetime=datetime.fromtimestamp(1635512400))

        assert resp.status_code == httpx.codes.OK
        history = resp.json()

        with open('./report.txt', 'w') as write_file:
                write_file.write(str(history))



