#!/bin/bash/python
#
# file: 1-backtest-sol.py
# abstract: solution for 1-backtest.md
#

import sys
import httpx
import json
from tda.auth import easy_client
from tda.client import Client
from datetime import datetime, timedelta

c = easy_client(
        api_key=str(sys.argv[1]),
        redirect_uri='https://localhost',
        token_path='./token')

# tickers = ["APPL", "GME", "GOOG"]
tickers = ["APPL"]

# datetime object
obj_datetime_start = datetime.now() - timedelta(days=1, microseconds=0)
# obj_datetime_start = datetime.now() - timedelta(days=30, microseconds=0)
obj_datetime_stop  = datetime.now() - timedelta(hours=12, microseconds=0)
# obj_datetime_stop = obj_datetime_start - timedelta(hours=12, microseconds=0)

print("start: {}".format(obj_datetime_start.strftime("%D %H:%m:%S")))
print("stop:  {}".format(obj_datetime_stop.strftime("%D %H:%m:%S")))

for item in tickers:

        resp = c.get_price_history('AAPL',
                period_type=Client.PriceHistory.PeriodType.DAY,
                period=Client.PriceHistory.Period.ONE_DAY,
                frequency_type=Client.PriceHistory.FrequencyType.MINUTE,
                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                start_datetime=obj_datetime_start,
                end_datetime=obj_datetime_stop
                )

        assert resp.status_code == httpx.codes.OK
        history = resp.json()

        # Like JSON better
        with open('./report.json', 'w') as write_file:
                write_file.write(json.dumps(history, indent=4))

        # with open('./report.txt', 'w') as write_file:
        #         write_file.write(str(history))



